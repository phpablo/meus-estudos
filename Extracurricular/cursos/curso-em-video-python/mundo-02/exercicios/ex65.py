print('-'*30)
print('Maior e menor')
print('-'*30)
total = soma = maior = menor = 0
is_out = True
while is_out:
    res = int(input('Digite um número :'))
    total += 1
    maior = res if res > maior else maior
    menor = res if res < maior else menor
    soma += res
    res2 = input('Quer continuar ? [ S / N ] ')
    
    if res2 == 'n' or res2 == 'N':
        is_out = False

media = soma / total
print(f' Vc digitou {total} numeros e a média foi {media}')
print(f' O maior valor foi {maior} e o menor valor foi {menor}')
    


