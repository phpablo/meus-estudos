'''
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
'''

pessoa = list()
dado = list()
gordo = magro = 0
while True:
  dado.append(str(input('Nome : ')))
  dado.append(float(input('Peso : ')))
  pessoa.append(dado[:])
  if gordo < dado[1]:
    gordo = dado[1]
  if magro > dado[1] or magro == 0:
    magro = dado[1]
  dado.clear()
  res = str((input('Quer continuar? [S / N]')))
  
  if res in 'Nn':
    break
print(f'Total de pessoas cadastradas foi {len(pessoa)}')
print(f'O maior peso foi de {gordo}Kg. Peso de ', end='')
for p in pessoa:
  if p[1] == gordo:
    print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {magro}Kg. Peso de ', end='')
for p in pessoa:
  if p[1] == magro:
    print(f'[{p[0]}] ', end='')