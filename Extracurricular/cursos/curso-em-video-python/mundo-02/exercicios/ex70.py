print('-=' * 30)
print('LOJA SUPER BARATÃO DOS DEVS'.center(60)) # Centraliza o título
print('-=' * 30)

total_spent = 0
expensive_count = 0
cheapest_name = ''
cheapest_price = float('inf') # Inicializa com "infinito" para garantir que o 1º preço seja menor

while True:
    product_name = input('Nome do produto: ').strip()
    
    # Alterado para float para aceitar centavos (ex: 10.50)
    product_price = float(input('Preço do produto: R$ '))

    # Soma o total e conta produtos acima de R$ 1000
    total_spent += product_price
    if product_price > 1000:
        expensive_count += 1

    # Lógica corrigida: descobre o produto mais barato
    if product_price < cheapest_price:
        cheapest_price = product_price
        cheapest_name = product_name

    # Validação de entrada para continuar
    while True:
        res = input('Quer continuar? [S/N] ').strip().upper()[0:1]
        if res in 'SN' and res != '':
            break
        print('Resposta inválida. Por favor, digite S ou N.')

    if res == 'N':
        break

print('-=' * 30)
print('FIM DO PROGRAMA'.center(60))
print('-=' * 30)

print(f'O total de compras foi R$ {total_spent:.2f}')
print(f'Temos {expensive_count} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi "{cheapest_name}" e custou R$ {cheapest_price:.2f}')