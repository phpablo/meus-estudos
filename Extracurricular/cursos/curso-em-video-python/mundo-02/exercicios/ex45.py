import random
from time import sleep

usuario = random.randint(1, 4)
jogador = random.randint(1, 4)
print(f'JOKENPÔ')
print(f'-='*25)
print('Escolha sua jogada')
print('1 - Pedra\n2 - Papel\n3 - Tesoura')
print('='*50)
if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
if usuario == 1:
    usuario = 'Pedra'
elif usuario == 2:
    usuario = 'Papel'
elif usuario == 3:
    usuario = 'Tesoura'

if usuario == jogador:
    resultado = 'Empate'
elif (usuario == 'Pedra' and jogador == 'Tesoura') or (usuario == 'Papel' and jogador == 'Pedra') or (usuario == 'Tesoura' and jogador == 'Papel'):
    resultado = 'Usuário venceu'
else:    
    resultado = 'Computador venceu'
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print(f'-='*25)
print(f'Jogada do usuário: {usuario}')
print(f'Jogada do computador: {jogador}')
print(f'Resultado: {resultado}')

