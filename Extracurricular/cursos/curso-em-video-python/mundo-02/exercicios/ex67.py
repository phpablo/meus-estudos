print('-'*30)
print('Break')
print('-'*30)

while True:
    res = int(input('Quer ver a tabuada de qual valor ? '))
    if res <= 0:
        print('TABUADA ENCERRADA! Volte sempre')
        break
    i = 1
    while i <= 10: 
        print(f'{res} x {i} = {res*i}')
        i += 1
    print('-='*30)



