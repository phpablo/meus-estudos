for p in range(1,5):
    nome = input(f'Digite o nome da {p}ª pessoa: ')
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo = input(f'Digite o sexo da {p}ª pessoa (M/F): ').upper()
    if p == 1:
        maior_idade = idade
        nome_mais_velho = nome
        contador_mulheres = 0
    else:
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
        if sexo == 'F' and idade < 20:
            contador_mulheres += 1
print(f'A pessoa mais velha é {nome_mais_velho} com {maior_idade} anos.')
print(f'O número de mulheres com menos de 20 anos é {contador_mulheres}.')