from random import randint
print('-'*30)
print("LISTAGEM DE PREÇOS".center(30))
print('-'*30)
products = ('Pao',1,'Queijo',5.00,'Salame',8.90)
for pos in range(0, len(products)):
  if pos % 2 == 0:
    print(f'{products[pos]:.<20}', end='')
  else:
    print(f'R${products[pos]:>7.2f}')
