print('-'*30)
print('Parada no input')
print('-'*30)
qtd = 1
teclado = int(input('digite: '))
total = teclado

while teclado != 999:
    teclado = int(input('digite: '))
    if teclado != 999:
        qtd += 1
        total += teclado
    else:
        break
print(f'vc digitou {qtd} numeros. e a soma deles é {total}')
print('FIM')
