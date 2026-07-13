sum_eighteen_age = sum_men = sum_twenty_age = 0

while True:
    print('-='*30)
    print('CADASTRE UMA PESSOA')
    print('-='*30)
    age = int(input('Idade: '))
    sexo = input('Sexo: [ M / F ] ').upper()
    while sexo not in 'MF':
        sexo = input('Sexo: [ M / F ] ').upper()
    
    sum_eighteen_age += 1 if age > 18 else 0
    sum_men += 1 if sexo == 'M' else 0
    sum_twenty_age += 1 if sexo == 'F' and age < 20 else 0
    res = input(f'Quer continuar ? [ S / N ] ').upper()
    
    while res not in 'SN':
        res = input(f'Quer continuar ? [ S / N ] ').upper()
    if res == 'S':
        continue
    else:
        break
print('='*10,'FIM DO PROGRAMA','='*10)
print(f'Total de pessoas com mais de 18 anos : {sum_eighteen_age}')
print(f'Ao todo temos {sum_men} homens cadastrados')
print(f'E temos {sum_twenty_age} mulheres com menos de 20 anos')

    


# RECEBER IDADE
# RECEBER SEXO { M OR F
# verificação se digiar o sexo errado difernte de f ou m ele pede somente os sexo denovo ou idadde denovo 

# RETURN
    # total pessoas maior de 18
    # total homens cadastrados
    # total mulheres com menos de 20 anos
# CADA CADASTRO PERGUNTA SE QUER CONTINUAR 
