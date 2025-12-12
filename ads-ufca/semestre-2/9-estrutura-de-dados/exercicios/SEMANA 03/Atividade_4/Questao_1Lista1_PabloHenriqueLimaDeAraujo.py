# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
quantidade_termos = int(input("Digite a quantidade de termos da PA: "))
razao = int(input("Digite a razão da PA: "))

pa = []
termo_atual = primeiro_termo

for _ in range(quantidade_termos):
    pa.append(termo_atual)
    termo_atual = termo_atual + razao

# Calcula a soma dos elementos da lista
soma_pa = sum(pa)

# Imprime os resultados
print("\nOs termos da Progressão Aritmética são:")
print(pa)
print("\nA soma dos termos da PA é:")
print(soma_pa)


