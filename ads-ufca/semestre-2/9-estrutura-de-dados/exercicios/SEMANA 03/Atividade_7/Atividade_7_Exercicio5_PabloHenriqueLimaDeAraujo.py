voos_cadastrados = {}

print("--- Etapa 1: Cadastro de Voos ---")
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
    print(f"Voo {numero_voo} cadastrado com sucesso!")

# --------------------------------------------------------------------
# --- Início da Funcionalidade da Questão 5 ---
# --------------------------------------------------------------------

print("\n\n--- Etapa 2: Modificação de Voos ---")
print('Instrução: Digite "fim" no número do voo para encerrar as modificações.')
print("-" * 45)

# 3 - Modificação de Dados
# loop para permitir a alteração de voos cadastrados
while True:
    voo_para_modificar = input("\nDigite o número do voo que deseja alterar: ")

    # condicao de parada do loop de modificação
    if voo_para_modificar.lower() == 'fim':
        break

    # verifica se o voo a ser modificado realmente existe no dicionario
    if voo_para_modificar not in voos_cadastrados:
        print(f"Erro: O voo '{voo_para_modificar}' não foi encontrado. Verifique a listagem e tente novamente.")
        continue  # volta para o início do loop de modificação

    # se o voo existe, mostra os dados atuais
    print(f"Alterando o voo: {voo_para_modificar}")
    print(
        f"Dados atuais -> Origem: {voos_cadastrados[voo_para_modificar]['origem']}, Destino: {voos_cadastrados[voo_para_modificar]['destino']}")

    # pergunta ao usuário o que ele deseja alterar
    nova_origem = input("Digite a NOVA origem (ou pressione Enter para não alterar): ")
    nova_destino = input("Digite o NOVO destino (ou pressione Enter para não alterar): ")

    # atualiza os valores apenas se o usuário digitou algo
    if nova_origem != "":
        voos_cadastrados[voo_para_modificar]['origem'] = nova_origem
        print("-> Origem alterada com sucesso!")

    if nova_destino != "":
        voos_cadastrados[voo_para_modificar]['destino'] = nova_destino
        print("-> Destino alterado com sucesso!")

    # mostra o resultado final da alteração
    print(
        f"Dados atualizados -> Origem: {voos_cadastrados[voo_para_modificar]['origem']}, Destino: {voos_cadastrados[voo_para_modificar]['destino']}")

# 4 - Exibição da Listagem Final
print("\n" + "=" * 55)
print("--- LISTAGEM FINAL DE VOOS CADASTRADOS ---")
print("=" * 55)

# verifica se o dicionario não está vazio
if not voos_cadastrados:
    print("Nenhum voo cadastrado.")
else:
    # cabeçalho da tabela
    print(f"{'NÚMERO DO VOO':<20} {'ORIGEM':<20} {'DESTINO':<20}")
    print("-" * 55)

    # percorre o dicionario e imprime cada voo de forma organizada
    for numero, dados in voos_cadastrados.items():
        print(f"{numero:<20} {dados['origem']:<20} {dados['destino']:<20}")

print("=" * 55)