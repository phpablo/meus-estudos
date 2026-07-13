### 1. Introdução e Configurações Iniciais
> **O que falar:**
> *"Olá! Eu fiquei responsável por explicar o **Emissor** da nossa aplicação. O objetivo principal dele é ler um arquivo local, dividi-lo em pedaços e enviá-lo de forma confiável usando o protocolo UDP, que por padrão não garante a entrega."*

*   **Configuração do Socket:** Criamos um socket UDP padrão (`SOCK_DGRAM`) e definimos um timeout de **1.0 segundo** (`sock.settimeout(1.0)`). Esse timeout é crucial porque, se não recebermos resposta do receptor nesse tempo, o emissor sabe que precisa retransmitir o pacote.
*   **Identificação Única:** Antes de iniciar, o emissor gera um **ID de Transação aleatório** (entre 1000 e 9999). Isso serve para o receptor saber que todos os pacotes pertencem ao mesmo arquivo. Iniciamos também o número de sequência (`seq_num`) em `0`.

---

### 2. Divisão do Arquivo e Cabeçalho Personalizado
> **O que falar:**
> *"Como o UDP envia datagramas brutos, nós dividimos o arquivo em blocos de bytes e adicionamos um cabeçalho customizado para garantir o controle da transmissão."*

*   **Divisão em Payloads:** Lemos o arquivo em pedaços de no máximo **1024 bytes**.
*   **Cabeçalho de 9 Bytes:** Para cada pedaço lido, nós empacotamos um cabeçalho usando a biblioteca `struct` com o formato `!IIB` (9 bytes no total):
    1.  **Número de Sequência (4 bytes - Inteiro):** Identifica a ordem do pacote.
    2.  **ID da Transação (4 bytes - Inteiro):** Garante que o pacote é do arquivo correto.
    3.  **Flag (1 byte):** Enviamos `0` para pacotes normais e `1` quando for o último pedaço do arquivo.

---

### 3. Protocolo Stop-and-Wait e Controle de Erros (Retransmissões)
> **O que falar:**
> *"Para garantir que nenhum pacote seja perdido, nós implementamos o clássico protocolo Stop-and-Wait com um limite de tentativas."*

*   **Parar e Esperar:** O emissor envia o pacote e entra em um loop aguardando o **ACK** (confirmação de recebimento) de 4 bytes enviado pelo receptor.
*   **Confirmação do ACK:** Só avançamos para o próximo pacote se o número de sequência retornado no ACK for idêntico ao do pacote enviado. Se for correto, incrementamos o `seq_num` e passamos para a próxima leitura.
*   **Mecanismo de Retry (Até 5 tentativas):**
    *   Se ocorrer um `socket.timeout` (passar 1 segundo sem resposta) ou o ACK vier incorreto, o código captura a exceção, incrementa o contador de tentativas e retransmite o mesmo pacote.
    *   **Segurança:** Caso atinja o limite máximo de **5 tentativas** sem nenhum sucesso, o emissor aborta a transmissão para não travar a aplicação em um loop infinito.

---

### 4. Finalização e Estatísticas de Performance
> **O que falar:**
> *"Após confirmar o último pacote (onde a Flag é igual a 1), nós encerramos a conexão e apresentamos uma métrica de desempenho."*

*   Ao final do envio bem-sucedido, o emissor calcula o tempo total gasto usando `time.perf_counter()`.
*   Ele exibe no terminal o tempo de execução e a **taxa de transferência efetiva em Mbps** (Megabits por segundo), dividindo o tamanho total do arquivo em bits pelo tempo decorrido. Isso nos ajuda a medir o impacto e a eficiência do nosso protocolo de confiabilidade sobre o UDP.