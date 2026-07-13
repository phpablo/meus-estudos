# --- Consulta de Atores por Série ---

# 1 - Base de Dados
# dicionario para armazenar as séries e seus atores. A estrutura será:
# { 'nome da serie': ['ator 1', 'ator 2', 'ator 3', ...] }
series_cadastradas = {
    'La Casa de Papel': ['Úrsula Corberó', 'Álvaro Morte', 'Itziar Ituño'],
    'Stranger Things': ['Millie Bobby Brown', 'Finn Wolfhard', 'Winona Ryder', 'David Harbour'],
    'The Witcher': ['Henry Cavill', 'Anya Chalotra', 'Freya Allan'],
    'Dark': ['Louis Hofmann', 'Lisa Vicari', 'Andreas Pietschmann'],
    'Breaking Bad': ['Bryan Cranston', 'Aaron Paul', 'Anna Gunn']
}

print("--- Sistema de Consulta de Séries ---")
print("Séries disponíveis em nossa base de dados:")
# imprime as chaves (nomes das séries) para o usuário saber o que pode consultar
for serie in series_cadastradas.keys():
    print(f"- {serie}")
print("-" * 45)

# 2 - Lógica de Consulta
# loop para permitir que o usuário faça várias consultas
while True:
    # solicita ao usuário o nome da série que ele deseja consultar
    serie_buscada = input("\nDigite o nome da série para ver os atores (ou 'fim' para sair): ")

    # condicao de parada do loop
    if serie_buscada.lower() == 'fim':
        break

    # busca pela série no dicionario.
    # o método .get() é uma forma segura de acessar uma chave.
    # se a chave existe, ele retorna o valor. se não, retorna None (ou um valor padrão).
    atores = series_cadastradas.get(serie_buscada)

    # 3 - Exibição do Resultado
    # verifica se a busca retornou um resultado ou não
    if atores:
        # se 'atores' não for None, a série foi encontrada
        print(f"\n--- Atores Principais de '{serie_buscada}' ---")
        # percorre a lista de atores e imprime cada um
        for ator in atores:
            print(f"-> {ator}")
        print("-" * 45)
    else:
        # se 'atores' for None, a série não está no dicionario
        print(f"Desculpe, a série '{serie_buscada}' não foi encontrada em nossa base de dados.")

print("\n--- Consulta encerrada. ---")
