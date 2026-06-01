'''
 Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for i in range(0,3):
  for j in range(0,3):
    matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('Matriz: ')
for i in range(0,3):
  for j in range(0,3):
    print(f'[{matriz[i][j]:^5}]', end='')
    if matriz[i][j] % 2 == 0:
      spar += matriz[i][j]
  print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for i in range(0,3):
  scol += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for j in range(0,3):
  if j == 0:
    mai = matriz[1][j]
  elif matriz[1][j] > mai:
    mai = matriz[1][j]
print(f'O maior valor da segunda linha é {mai}')

