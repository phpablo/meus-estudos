# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

import random

compradores = []

print("--- Cadastro da Rifa ---")
print('(Digite "fim" para encerrar o cadastro e realizar o sorteio)')

while True:
    nome = input("Digite o nome do comprador: ")
    if nome.lower() == "fim":
        break
    compradores.append(nome)

ganhador = random.choice(compradores)
print("\n--- Sorteio Realizado! ---")
print(f"O grande ganhador(a) da rifa é: {ganhador}")

