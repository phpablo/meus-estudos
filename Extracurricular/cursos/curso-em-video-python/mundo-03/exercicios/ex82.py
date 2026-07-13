'''
Exercício Python 082: 

Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
7,9,2,6,8

'''
lista = list()
even = list()
odd = list()
while True:
    lista.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar ? [ S / N ] ')).strip().upper()
    if res == 'N':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
'''for num in lista:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
'''
print(f"\nA lista completa é {lista}")
print(f"\nA lista de pares é {even}")
print(f"\nA lista de impares é {odd}")
