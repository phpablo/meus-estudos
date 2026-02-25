mas = 'M'
fem = 'F'
c = True

while c :
    print('Digite S para sair!')
    res = input('Digite seu sexo: M ou F:').upper()
    if res == 'S':
        c = False
    elif res != 'M' and res != 'F':
        print('Entrada inválida. Por favor, digite apenas M ou F.')
        
