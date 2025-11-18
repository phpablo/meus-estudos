from Q3_Semana1 import Ponto

lista_pontos = []

while True:
    nome = input("Digite o nome do ponto (ou ENTER para sair): ")
    if nome == "":
        break

    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))

    ponto = Ponto(nome, x, y)
    lista_pontos.append(ponto)

print("\n--- Pontos cadastrados ---")
for p in lista_pontos:
    print(p)
