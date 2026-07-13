'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

impar = list()
par = list()
for i in range(0,7):
  res = int(input(f'{i+1}º número: '))
  if res % 2 == 0:
    par.append(res)
  else:
    impar.append(res)
tudo = [(impar),(par)]
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores impares digitados foram: {sorted(impar)}')


