from random import randint
print('-'*30)
print('Alatóriorio de Números')
print('-'*30)


num_lista = []
for i in range(1,6):
  num = randint(1,100)
  num_lista.append(num)
tupla = (num_lista)

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor foi {sorted(tupla)[4]}')
print(f'O menor valor foi {sorted(tupla)[0]}')
