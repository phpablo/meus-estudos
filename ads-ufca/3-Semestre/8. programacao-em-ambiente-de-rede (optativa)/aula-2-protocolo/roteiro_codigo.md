"Como o UDP é um protocolo não-confiável por padrão — ou seja, ele envia pacotes mas não garante a entrega nem a ordem —, nós criamos o nosso próprio Módulo de Confiabilidade por cima dele. Ele funciona através de duas  engrenagens principais:                                                                                  
1. A primeira é o Cabeçalho Personalizado de 9 bytes: Nele, inserimos um Número de Sequência para ordenar os pacotes e evitar duplicatas, um ID de Transação para identificar o arquivo e uma Flag que avisa quando o arquivo terminou
                                                     
2. A segunda é o mecanismo de Stop-and-Wait (Parar e Esperar): O emissor envia um pacote e espera um ACK (confirmação) do receptor. Se o receptor não responder dentro de um tempo limite (Timeout), o emissor retransmite o pacote automaticamente                                                                                
Por fim, se a conexão cair de vez, o receptor executa um Rollback, deletando o arquivo incompleto para evitar corrupção de dados. Assim, garantimos uma transferência 100% segura usando UDP!

 ### 🎙️ Roteiro de Fala (Foco em Retry e Descarte)           
Agora, para lidar com as falhas na rede, nós implementamos duas estratégias essenciais 

A primeira é o mecanismo de Retry (Retransmissão) no Emissor. Quando enviamos um pacote, estabelecemos um limite de tempo para receber a confirmação. Se esse tempo expira e não recebemos o ACK, o código assume que o pacote se perdeu e tenta reenviá-lo. 

Definimos um limite de 5 tentativas para cada pacote. Se após 5 tentativas a rede continuar fora do ar, o envio é abortado por segurança para não prender o programa em um loop infinito

A segunda estratégia é o Rollback no Receptor. Se o emissor cair no meio da transmissão, o receptor não pode ficar esperando para sempre e nem deve salvar um arquivo corrompido ou incompleto. Por isso, definimos um timeout de 10 segundos. Se o receptor ficar 10 segundos sem receber novos dados, ele assume que a transmissão falhou, fecha o arquivo e apaga o arquivo incompleto do disco (usando a função  os.remove ). Isso garante que o sistema de arquivos do receptor nunca fique poluído com arquivos inúteis.