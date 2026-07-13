vetor = [5, 10, 20, 30]
novo = int(input("Digite o número para inserir: "))

posicao = 0
while posicao < len(vetor) and vetor[posicao] < novo:
    posicao += 1

vetor.insert(posicao, novo)

print("Vetor atualizado:", vetor)