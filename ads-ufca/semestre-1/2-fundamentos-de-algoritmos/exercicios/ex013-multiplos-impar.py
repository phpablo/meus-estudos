# Escreva um programa que receba um inteiro positivo e imprime na tela quantos divisores impares ele tem.
print("SEQUENCIA DE 3 NUMEROS NEGATIVOS")
print("================================")

inteiro = int(input("\nInforme um número inteiro positivo :"))
count = 0
for i in range(1,inteiro+1,2):
    if inteiro % i == 0:
        count += 1
print("O numero %d possui %d divisores ímpares" % (inteiro, count))


print("================================")
print("         FIM PROGRAMA           ")