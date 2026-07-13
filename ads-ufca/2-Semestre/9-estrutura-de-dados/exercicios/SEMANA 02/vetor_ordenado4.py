vetor = [1,2,3,4,5,6]

novo_valor = int(input("Digite um numero:"))

posicao = 0
while posicao < len(vetor) and vetor[posicao] < novo_valor:
    posicao += 1

vetor.insert(posicao, novo_valor)

print("Novo vetor com valor inserido que o usuário digitou", vetor)