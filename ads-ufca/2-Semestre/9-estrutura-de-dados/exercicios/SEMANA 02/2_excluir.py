vetor = [10, 20, 30, 40, 50]
valor = int(input("Digite o valor que deseja excluir: "))

inicio = 0
fim = len(vetor) -1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == valor:
        posicao = meio
        break
    elif vetor[meio] < valor:
        inicio = meio + 1
    else:
        fim = meio - 1

if posicao == -1:
    print("Valor não encontrado no vetor.")
else :
    vetor.pop(posicao)
    print("Vetor após exclusão:", vetor)
vetor = [5, 15, 25, 35, 45]
print("Vetor inicial:", vetor)

valor = int(input("Digite o valor que deseja excluir: "))

# Pesquisa binária
inicio, fim = 0, len(vetor) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == valor:
        posicao = meio
        break
    elif vetor[meio] < valor:
        inicio = meio + 1
    else:
        fim = meio - 1

# Exclusão e reorganização
if posicao != -1:
    vetor.pop(posicao)
    print("Vetor após exclusão:", vetor)
else:
    print("Valor não encontrado.")


