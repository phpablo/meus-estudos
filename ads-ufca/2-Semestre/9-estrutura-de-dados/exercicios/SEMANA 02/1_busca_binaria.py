vetor = [5, 10, 15, 20, 25, 30, 35]
n1 = 25

inicio = 0
fim = len(vetor) -1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == n1:
        encontrado = True
        break
    elif vetor[meio] < n1:
        inicio = meio +1
    else:
        fim = meio -1
if encontrado:
    print(f'Valor {n1} encontrado na posicao {meio}')
else:
    print(f' Valor {n1} não encontrado')