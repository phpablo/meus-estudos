# Escreva um programa que receba um inteiro positivo e imprime todas as somas iguais a de N de 2 números inteiros
# positivos distintos sem repetição

print("SEQUENCIA POSITIVA DISTINTAS")
print("================================")

n = int(input("Insira um número inteiro positivo:\n"))

for n1 in range (2,n+1):
    for n2 in range(n1+1, n+1):
        coprimos = True
        for i in range(2,n1+1):
            if (n1 % 1 == 0) and (n2 % i == 0):
                coprimos = False
                break # Sai apenas do for mais interno
        if coprimos:
            print(n1,n2)






print("================================")
print("         FIM PROGRAMA           ")