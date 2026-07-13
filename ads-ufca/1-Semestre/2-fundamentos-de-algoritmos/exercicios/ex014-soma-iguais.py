# Escreva um programa que receba um inteiro positivo e imprime todas as somas iguais a de N de 2 números inteiros
# positivos distintos sem repetição

print("SEQUENCIA POSITIVA DISTINTAS")
print("================================")

n1 = int(input("Insira um número inteiro positivo:\n"))

for i in range(1, n1):
    for j in range(1,n1):
        if (i+j==n1) and (i != j):
            print("%d + %d = %d " % (i,j,n1))






print("================================")
print("         FIM PROGRAMA           ")