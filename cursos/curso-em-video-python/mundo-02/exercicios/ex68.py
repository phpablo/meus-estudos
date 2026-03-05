from random import randint
print('-='*30)
print('PAR OU IMPAR')
print('-='*30)
win = 0

while True :
    robot = randint(1,10)
    res = int(input('Diga um valor: '))
    choose = input('Par ou Impar ? [ P / I]').upper()
    tot = res + robot
    if choose == 'P':
        is_even = True if tot % 2 == 0 else False
        if not is_even:
            print('-'*30)
            print(f'Voce jogou {res} e o robo {robot}. Total de {tot} e DEU IMPAR')
            print(f'Voce PERDEU\nGAME OVER! Voce venceu {win} vezes')
            break
        win +=1
        print('-'*30)
        print(f'Voce jogou {res} e o robo {robot}. Total de {tot} e DEU PAR')
        print(f'Voce VENCEU\nVamos jogar novamente!')
        continue
    elif choose == 'I':
        is_odd = True if tot % 2 != 0 else False
        if not is_odd:
            print('-'*30)
            print(f'Voce jogou {res} e o robo {robot}. Total de {tot} e DEU PAR')
            print(f'Voce PERDEU\nGAME OVER! Voce venceu {win} vezes')
            break
        win +=1
        print('-'*30)
        print(f'Voce jogou {res} e o robo {robot}. Total de {tot} e DEU IMPAR')
        print(f'Voce VENCEU\nVamos jogar novamente!')
        continue
    else:
        print('Escolha inválida! Escolha P para PAR ou I para IMPAR')