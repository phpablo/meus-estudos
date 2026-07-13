# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo


import random

print("--- Verificador de Matriz Diagonal ---")
try:
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")
    exit()

matriz_m = []
for i in range(linhas):
    linha_atual = []
    for j in range(colunas):
        elemento_aleatorio = random.randint(0, 9)
        linha_atual.append(elemento_aleatorio)
    matriz_m.append(linha_atual)

print("\nMatriz M gerada:")
if not matriz_m:
    print("[]")
else:
    for linha in matriz_m:
        print(f"\t{linha}")

a_matriz_eh_diagonal = True

if linhas != colunas or linhas == 0:
    a_matriz_eh_diagonal = False
else:
    for i in range(linhas):
        for j in range(colunas):
            if i != j and matriz_m[i][j] != 0:
                a_matriz_eh_diagonal = False
                break

        if not a_matriz_eh_diagonal:
            break

print("\n--- Análise ---")
if a_matriz_eh_diagonal:
    print("O resultado da análise é: a matriz M É uma matriz diagonal.")
else:
    print("O resultado da análise é: a matriz M NÃO é uma matriz diagonal.")

