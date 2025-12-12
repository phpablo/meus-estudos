# --- Filtro de Funcionários ---

# 1 - Base de Dados
# lista de dicionarios para armazenar os dados da tabela de funcionários.
# cada dicionario representa um funcionário.
funcionarios = [
    {'nome': 'Ana Silva', 'sexo': 'Feminino', 'setor': 'TI', 'salario': 5500.00},
    {'nome': 'Bruno Costa', 'sexo': 'Masculino', 'setor': 'TI', 'salario': 4800.00},
    {'nome': 'Carla Dias', 'sexo': 'Feminino', 'setor': 'RH', 'salario': 3200.00},
    {'nome': 'Daniel Martins', 'sexo': 'Masculino', 'setor': 'Financeiro', 'salario': 6000.00},
    {'nome': 'Elisa Ferreira', 'sexo': 'Feminino', 'setor': 'TI', 'salario': 2800.00},
    {'nome': 'Fernanda Lima', 'sexo': 'Feminino', 'setor': 'TI', 'salario': 7100.00},
    {'nome': 'Gustavo Borges', 'sexo': 'Masculino', 'setor': 'Vendas', 'salario': 3100.00},
    {'nome': 'Helena Souza', 'sexo': 'Feminino', 'setor': 'TI', 'salario': 3050.50}
]

# 2 - Processamento e Filtragem
# lista para armazenar apenas as funcionárias que atendem aos critérios
mulheres_ti_acima_3000 = []

# percorre cada dicionario (funcionário) na lista principal
for funcionario in funcionarios:
    # verifica se todas as condições são verdadeiras para o funcionário atual
    if (funcionario['sexo'] == 'Feminino' and
            funcionario['setor'] == 'TI' and
            funcionario['salario'] > 3000.00):
        # se todas as condições forem atendidas, adiciona o dicionario do funcionário à lista de resultados
        mulheres_ti_acima_3000.append(funcionario)

# 3 - Exibição do Resultado
print("=" * 60)
print("--- Listagem de Mulheres do Setor de TI com Salário > R$ 3.000,00 ---")
print("=" * 60)

# verifica se a lista de resultados não está vazia
if not mulheres_ti_acima_3000:
    print("Nenhuma funcionária encontrada com os critérios especificados.")
else:
    # cabeçalho da tabela de resultados
    print(f"{'NOME':<25} {'SETOR':<10} {'SALÁRIO (R$)'}")
    print("-" * 60)

    # percorre a lista de resultados e imprime os dados de cada funcionária
    for funcionaria in mulheres_ti_acima_3000:
        # formata a saída para alinhar os dados em colunas
        print(f"{funcionaria['nome']:<25} {funcionaria['setor']:<10} {funcionaria['salario']:>12,.2f}")

print("-" * 60)
