'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''
list = []
while True:
    num = int(input('Digite um valor: '))
    if num not in list:
        list.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('=-'*30)
list.sort()
print(f'Os valores digitados foram: {list}')