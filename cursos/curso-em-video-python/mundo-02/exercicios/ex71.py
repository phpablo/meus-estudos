print('-=' * 30)
print('GRINGOTS'.center(60))
print('-=' * 30)

valor = int(input('Que valor você quer sacar ? R$ '))
total = valor
ced = 50
tot_ced = 0

while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break
print('-=' * 30)
print('Volte sempre ao GRINGOTS! Tenha um bom dia!')
            







