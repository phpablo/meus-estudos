print('===== Gohan Veículos - Relatório Final =====')
km = float(input('>>> Qual a quantidade de Km rodados? '))
dias = int(input('>>> Quantos dias você ficou com o carro? '))
preco_carro = 60 * dias
preco_km = 0.15 * km

preco_total = preco_carro + preco_km
print(f'\n\n====== RELATÓRIO TOTAL ======')
print(f'>>> Dias Alugado: {dias}')
print(f'>>> Km rodados: {km} km')
print("="*25)
print(f'Preço Total: R$ {preco_total:.2f}')
print(f'\n\n====== OBRIGADO PELA PREFERÊNCIA ======')










