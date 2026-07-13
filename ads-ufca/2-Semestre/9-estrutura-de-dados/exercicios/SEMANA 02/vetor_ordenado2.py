vetor = [10, 20, 30,50]
novo_valor = 40
print('================================')

posicao = 0

while posicao < len(vetor) and vetor[posicao] < novo_valor:
    posicao += 1

vetor.insert(posicao,novo_valor)

print(f'Vetor ordenado após a inserção:',vetor)