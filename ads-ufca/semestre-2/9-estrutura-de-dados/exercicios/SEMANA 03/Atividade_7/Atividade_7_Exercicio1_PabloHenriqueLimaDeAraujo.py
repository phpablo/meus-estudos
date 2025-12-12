# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo


dados_vendas = {}

print("--- Sistema de Lançamento de Vendas ---")
print("Instruções: Insira a razão social e o valor de cada venda.")
print('Digite "fim" no campo "Razão Social" para finalizar e gerar o relatório.')
print("-" * 50)

# 2. COLETA E ACUMULAÇÃO DE DADOS
# Loop infinito que só será interrompido quando o usuário digitar "fim".
while True:
    razao_social = input("\nDigite a Razão Social do cliente: ")

    # Condição de parada do loop (insensível a maiúsculas/minúsculas)
    if razao_social.lower() == 'fim':
        break

    # Validação da entrada do valor da compra
    try:
        valor = float(input(f"Digite o valor da compra para '{razao_social}': R$ "))
        # Garante que o valor não seja negativo
        if valor < 0:
            print("Erro: O valor da compra não pode ser negativo. Tente novamente.")
            continue
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número (ex: 150.50).")
        continue  # Volta para o início do loop


    if razao_social in dados_vendas:
        # Se o cliente já existe, soma o novo valor ao total
        dados_vendas[razao_social] += valor
    else:
        # Se é um cliente novo, cria a entrada no dicionário
        dados_vendas[razao_social] = valor

    print(f"Venda registrada! Novo total para '{razao_social}': R$ {dados_vendas[razao_social]:.2f}")


# Verifica se algum dado foi inserido antes de tentar ordenar
if dados_vendas:
    relatorio_ordenado = sorted(dados_vendas.items(), key=lambda item: item[1], reverse=True)


    print("\n\n" + "=" * 55)
    print("--- RELATÓRIO FINAL DE CLIENTES POTENCIAIS ---")
    print("(Ordenado por maior valor total de compras)")
    print("=" * 55)
    # Cabeçalho da tabela
    print(f"{'#':<5} {'RAZÃO SOCIAL':<30} {'VALOR TOTAL COMPRADO':>18}")
    print("-" * 55)

    # Itera sobre a lista ordenada para exibir cada cliente
    for i, (cliente, total) in enumerate(relatorio_ordenado, start=1):
        # Formata a linha para que os dados fiquem alinhados em colunas
        print(f"{str(i):<5} {cliente:<30} R$ {total:>15,.2f}")

    print("-" * 55)
else:
    # Mensagem para o caso de nenhum dado ter sido inserido
    print("\nNenhum dado de venda foi inserido. O relatório está vazio.")

