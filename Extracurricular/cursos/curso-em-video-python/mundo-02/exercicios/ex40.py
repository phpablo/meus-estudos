# somar duas notas
# calcular media
# abaixo 5.0 reprovado
# entre 5.0 e 6.9 recuperacao
# 7.0 ou maior, aprovado

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('REPROVADO')
elif m >= 5.0 and m < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
