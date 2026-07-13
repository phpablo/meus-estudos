voos_cadastrados = {}

print("--- Sistema de Cadastro de Voos ---")
print('Instrução: Digite "fim" no número do voo para encerrar o cadastro.')
print("-" * 45)

# 2 - Coleta de Dados
# loop para cadastrar os voos
while True:
    numero_voo = input("\nDigite o número do voo (ex: G3-1405): ")

    # condicao de parada do loop
    if numero_voo.lower() == 'fim':
        break

    # verifica se a chave (numero_voo) já existe
    if numero_voo in voos_cadastrados:
        print(f"Erro: O voo '{numero_voo}' já foi cadastrado. Tente um número diferente.")
        continue  # volta para o inicio do loop

    # solicita a origem e o destino do voo
    origem = input(f"Digite a origem do voo '{numero_voo}': ")
    destino = input(f"Digite o destino do voo '{numero_voo}': ")

    # armazena os dados no dicionario principal
    voos_cadastrados[numero_voo] = {'origem': origem, 'destino': destino}
    print(f"Voo {numero_voo} (Origem: {origem}, Destino: {destino}) cadastrado com sucesso!")

# 3 - Processamento e Contagem
# contador para armazenar a quantidade de voos que partem de Natal
contador_origem_natal = 0

# percorre os valores (que são outros dicionários) do dicionario principal
for dados_voo in voos_cadastrados.values():
    # verifica se o valor da chave 'origem' é igual a 'Natal' (ignorando maiusculas/minusculas)
    if dados_voo['origem'].lower() == 'natal':
        contador_origem_natal += 1  # incrementa o contador

# 4 - Exibição do Resultado
print("\n" + "=" * 50)
print("--- Análise de Voos Concluída ---")

# exibe o resultado final da contagem
print(f"A quantidade de voos cadastrados com origem em Natal é: {contador_origem_natal}")

print("=" * 50)
