# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

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