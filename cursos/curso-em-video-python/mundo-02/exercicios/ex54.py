from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        totmenor += 1
    else:
        totmaior += 1
        print (f'Quem nasceu em {nasc} tem {idade} anos em {atual} e é MAIOR DE IDADE')


print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')