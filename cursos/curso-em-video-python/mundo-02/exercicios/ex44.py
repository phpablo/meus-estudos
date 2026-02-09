import random

preco_original = random.randrange(10, 100)
print(f'Preço do Produto: R$ {preco_original:.2f}')
print('='*50)
print('Escolha uma forma de pagamento')
print('1 - À vista (10% desc)\n2 - À vista no cartão (5% desc)\n3 - 2x no cartão (Preço normal)\n4 - 3x ou mais (20% juros)')
print('='*50)

forma_pagamento = random.randint(1, 4)

match forma_pagamento:
    case 1:
        print('Selecionado: À vista')
        preco_final = preco_original * 0.90
    case 2:
        print('Selecionado: À vista no cartão')
        preco_final = preco_original * 0.95
    case 3:
        print('Selecionado: 2x no cartão')
        preco_final = preco_original
    case 4:
        print('Selecionado: 3x ou mais no cartão')
        preco_final = preco_original * 1.20

print(f'\nValor final do produto: R${preco_final:.2f}')