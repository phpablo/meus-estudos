print("================================\n")
print("CALCULADORA DE TRUE OR FALSE\n")
print("================================\n")
num1 = int(input("Digite um número:\n"))
num2 = int(input("Agora outro número: \n"))
num3 = int(input("um ultimo numero:\n"))
requisito1 = num1 >=10 and num1 <= 20
requisito2 = num2 >= num1 and num1 <= num3
requisto3  = num3 >=1 and num3 <= 30
resultado = requisito1 or requisito2 or requisto3

print('O resultado é ')
print(resultado)
print("================================\n")
print("         FIM PROGRAMA           \n")
print("================================\n")