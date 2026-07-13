preco = float(input('Digite o preço: '))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'O preço R$ {preco} com o desconto de 5% é {desconto}\n Valor final R$ {novo_preco}')
print('==============================================================')
# Refatorado

preco2 = float(input('Digite o preço: '))
novo_preco2 = preco2 - (preco * 5 / 100)
print(f'O preço R$ {preco2} Valor final R$ {novo_preco2}')








