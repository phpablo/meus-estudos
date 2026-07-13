# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

import random

print("--- Verificador de Matriz Nula ---")
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
        elemento_aleatorio = random.random()
        linha_atual.append(elemento_aleatorio)

    matriz_m.append(linha_atual)

print("\nMatriz M gerada:")
if not matriz_m:
    print("[]")
else:
    for linha in matriz_m:
        linha_formatada = [f"{elem:.3f}" for elem in linha]
        print(linha_formatada)

a_matriz_eh_nula = True

for linha in matriz_m:
    for elemento in linha:
        if elemento != 0:
            a_matriz_eh_nula = False
            break

    if not a_matriz_eh_nula:
        break

print("\n--- Análise ---")
if a_matriz_eh_nula:
    print("O resultado da análise é: a matriz M É uma matriz nula.")
else:
    print("O resultado da análise é: a matriz M NÃO é uma matriz nula.")










