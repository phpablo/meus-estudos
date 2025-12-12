vetor = [10,20,30,65,78,7,8,9]

print(f'Vetor original: {vetor}')

res = int(input('Escolha um numero do vetor para excluir:\n'))

posicao = -1

for i in range(len(vetor)):
    if vetor[i] == res:
        posicao = i
        break

if posicao == -1:
    print('Valor não encontrado  no vetor.')
else:
    deslocamentos = 0

    for i in range(posicao, len(vetor)-1):
        vetor[i] = vetor[i + 1]
        deslocamentos += 1

    vetor.pop()
    print('Vetor após exclusão:',vetor)
    print('Deslocamentos:',deslocamentos)
    print('Tamanho do vetor',len(vetor))




