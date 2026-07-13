# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

# ATIVIDADE DO VETOR NÃO ORDENADO - INSERIR
# Esse é um vetor não ordenado
vetor = [5, 10, 15] # aqui vc cria um vetor e adiciona 3 elementos nele
print("Vetor inicial:", vetor) # aqui vc printa na tela todos os elemetos do vetor

# Função que insere no final o valor que vc quiser
vetor.append(20) # aqui eu estou adicionando ao final do vetor um elemento com valor de 20
print("Após inserção no final:", vetor) # ao printar, vai ter mais um elemento no final do vetor que adicionei ele na linha anterior

# Inserindo no meio agora
vetor.insert(1, 7)
# ao fazer isso, eu adiciono no índice 1 o valor 7, logo, os numeros que estão nos índices
# acima de 1 , são 'empurrados' pra direita pra esse entrar, então ele adiciona um elemento
# e atualiza a posição dos demais elementos que estão nos índices acima de 1 ( q foi onde ele entrou )
print("Após inserção no meio:", vetor) # mostro na tela o vetor completo com todas as inserções

# ATIVIDADE DO VETOR NÃO ORDENADO - PESQUISAR

# criei um vetor novo
vetor = [12, 7, 5, 20, 11, 8]
# pede pro usuario digitar o valor que ele quer pesquisar se existe no meu vetor
valor = int(input("Digite o valor que deseja pesquisar: "))

#crio uma variavel que vai controlar o loop for q vai verificar os elementos
encontrado = False

# aqui ele vai iterar sobre cada elemento do meu vetor
# em cada elemento que ele passar, ele vai comparar com o que o usuario digitou
# e se o elemento for igual ao digitado, ele muda o estado da varivael 'encontrado' para True
# então ele quebra o loop e passa pra proxima instrução
# se não for encontrado, ele nunca vai executar o primeiro if, mas a verificação vai ser feita
# e ele também pula pro  if fora do loop do FOR
for elemento in vetor:
    if elemento == valor:
        encontrado = True
        break

# aqui ele verifica se a variável 'encontrado' é verdadeira, se for, mostra na tela a mensagem
if encontrado:
    print(f"O valor {valor} foi encontrado!")
# se a variavel nao mudou para true, ela continua false, então ela entra no else dessa condição
# mostrando na tela a mensagem que o valor digitado não foi encontrado no vetor
else:
    print(f"O valor {valor} não está no vetor.")