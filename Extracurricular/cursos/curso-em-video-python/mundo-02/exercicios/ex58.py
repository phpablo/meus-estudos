from random import randint
computador = randint(0,10)
acertou = False
palpites = 0
print (f'Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10\nSerá que voce consegue adivinhar qual foi?')

# second way to do it
while not acertou:
    jogador = int(input(f'Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'Mais...tente mais uma vez')
        elif jogador > computador:
            print(f'Menos...tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns')

'''
while count:
    res = int(input(f'Qual seu palpite? 5'))
    tentativas += 1
    if res < num:
        print(f'Mais...tente mais uma vez')
        continue
    elif res > num:
        print(f'Menos...tente mais uma vez')
        continue
    else:
        print(f'Acertou com {tentativas} tentativas. Parabéns')
        count = False
'''
