print('-'*30)
print('Tabela Campeonato Brasileiro')
print('-'*30)
tabela = ('Palmeiras', 'Corinthians', 'Fluminense', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'América-MG', 'Botafogo', 'Bragantino', 'Santos', 'Goiás', 'Coritiba', 'São Paulo', 'Vasco da Gama', 'Ceará SC', 'Internacional', 'Grêmio', 'Fortaleza', 'Atlético-GO', 'Avaí')

# mostrar 5 primeiros colocados
print(f'Os 5 primeiros colocados são: {tabela[1:6]}')
print('-'*30)
# mostrar os 4 ultimos colocados
print(f'Os 4 ultimos colocados são: {tabela[-4:]}')
print('-'*30)
# lista com times de ordem alfabética
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-'*30)
# qual posição está a Fluminense 
print(f'A Fluminense está na {tabela.index("Fluminense")+1}ª posição.')