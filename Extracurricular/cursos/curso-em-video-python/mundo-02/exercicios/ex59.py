
num_one = int(input('Digite o primeiro valor: '))
num_two = int(input('Digite o segundo valor: '))
res = True
while res:
    print('='*50)
    print('MENU DE OPÇÕES')
    print('='*50)
    print('1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos numeros\n5 - Sair do programa')
    user = int(input('>>>> Qual a opção desejada ? '))

    if user == 5:
        print('-=-=-=-=-=-=-=-=-=-=-=')
        print('FIM DO PROGRAMA\n Volte Sempre')
        res = False
    elif user == 1:
        soma = num_one+num_two
        print(f'A soma de {num_one} + {num_two} é igual a {soma}')
    elif user == 2:
        mult = num_one * num_two
        print(f'A multiplicação de {num_one} x {num_two} é igual a {mult}')
    elif user == 3:
        if num_two > num_one:
            maior = num_two
        else:
            maior = num_one
        print(f'O maior entre {num_one} e {num_two} é {maior}')
    elif user == 4:
        print('Informe os números novamente')
        num_one = int(input('Digite o primeiro valor: '))
        num_two = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida. Tente novamente')

