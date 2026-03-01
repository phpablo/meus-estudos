n = int(input('Digite um numero para calcular o fatorial '))
c = n
f = 1
print(f'Calculando o fatorial de {n}')
while c > 0:
    print(f'{c}',end='')
    print(f' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')
