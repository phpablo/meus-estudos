# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

# ATIVIDADE DO VETOR ORDENADO - INSERIR E IMPRIMIR

# aqui eu tenho um vetor que já tá ordenado certinho, do menor pro maior
vetor = [10, 20, 30, 50]

# esse é o valor novo que eu quero colocar no vetor mantendo a ordem
novo_valor = 40

# aqui eu crio uma variável pra saber onde o valor novo deve entrar
posicao = 0
# esse while vai ficar rodanto até que
# eu ainda estiver dentro do tamanho do vetor
# e o valor que tá no vetor for menor que o que eu quero inserir
# quando isso for falso, significa que achei o lugar certo de colocar o novo valor
while posicao < len(vetor) and vetor[posicao] < novo_valor:
    # aqui eu avanço pro próximo índice enquanto o novo valor for maior
    posicao += 1
# aqui eu insiro o novo valor exatamente no índice encontrado acima
vetor.insert(posicao, novo_valor)

# aqui eu só printo o vetor já bonitinho, com o valor novo no lugar certo
print("Vetor ordenado após inserção:", vetor)
