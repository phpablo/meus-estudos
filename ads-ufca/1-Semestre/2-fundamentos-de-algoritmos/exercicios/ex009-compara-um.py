print("COMPARA NÚMERO")
print("================================")

n1 = int(input("\nDigite o primeiro número inteiro:"))
n2 = int(input("\nDigite o segundo número inteiro:"))
n3 = int(input("\nDigite o terceiro número inteiro:"))

if (n1 > n2) and (n1 < n3):
    print("O número maior é o primeiro")
elif n2 > n1 and n2 > n3:
    print("O número maior é o segundo")
else:
    print("O número maior é o terceiro")

print("================================")
print("         FIM PROGRAMA           ")