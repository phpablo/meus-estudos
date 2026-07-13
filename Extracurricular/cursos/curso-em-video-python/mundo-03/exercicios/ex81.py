'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista

A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista

'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar ? [S/N] '))
    if res in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')








'''
count = 0
list = []
while True:
    res = int(input('Digite um valor: '))
    count += 1
    list.append(res)
    res2 = input('Quer continuar ? [s/n]').lower()
    if res2 == 'n':
        break
isFive = 5 in list
list.sort(reverse=True)
print(f"\n Você digitou {count} elementos")
print(f'\n Decrescente: {list}')
if isFive:
    print(f'\n O valor 5 está na lista')
else:
    print(f'\n O valor 5 não foi encontrado na lista')
'''