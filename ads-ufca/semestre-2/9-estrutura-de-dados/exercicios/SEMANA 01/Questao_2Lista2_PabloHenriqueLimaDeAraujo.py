# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

# ATIVIDADE DO VETOR ORDENADO - EXCLUIR


vetor = [5, 15, 25, 35, 45]           # aqui eu tenho um vetor ordenado de boa, tudo certinho
print("Vetor inicial:", vetor)        # só mostrando na tela como ele tá antes de mexer

valor = int(input("Digite o valor que deseja excluir: "))  # peço pro usuário qual valor ele quer remover do vetor

# Pesquisa binária
inicio, fim = 0, len(vetor) - 1       # aqui eu defino onde começa e onde termina a busca binária
posicao = -1                          # essa variável vai guardar a posição do valor, caso eu ache. (-1 = não achei)

# aqui começa a busca binária, que só roda enquanto ainda tiver intervalo pra procurar
while inicio <= fim:
    meio = (inicio + fim) // 2        # calculo o meio do intervalo atual
    if vetor[meio] == valor:          # se o valor no meio for igual ao que quero excluir:
        posicao = meio                # guardo a posição onde ele tá
        break                         # e saio do loop porque já encontrei
    elif vetor[meio] < valor:         # se o valor do meio for menor do que quero excluir:
        inicio = meio + 1             # significa que o valor tá mais pra direita, então avanço o início
    else:
        fim = meio - 1                # se for maior, tá na esquerda, então recuo o fim

# Exclusão e reorganização
if posicao != -1:                     # se a posição mudou, quer dizer que achei o valor no vetor
    vetor.pop(posicao)                # aqui eu removo o valor pelo índice encontrado
    print("Vetor após exclusão:", vetor)  # mostro o vetor já com o elemento removido
else:
    print("Valor não encontrado.")    # se a posição ficou -1, quer dizer que não achei o valor no vetor
