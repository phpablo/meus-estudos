# Escreva um programa que receba um inteiro positivo e imprime todas as somas iguais a de N de 2 números inteiros
# positivos distintos sem repetição

print("SEQUENCIA POSITIVA DISTINTAS")
print("================================")

a = int(input('digit um numero inteiro maior que 1\n'))
b = int(input('digit outro numero inteiro maior que 1\n'))
for n in range(a,b+1):
    e_primo = True
    for i in range(2,n):
        if n % i == 0:
            e_primo = False
            break
    if e_primo:
        print("O número %d é primo" % n)





print("================================")
print("         FIM PROGRAMA           ")