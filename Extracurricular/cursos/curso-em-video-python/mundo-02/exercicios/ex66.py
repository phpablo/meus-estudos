print('-'*30)
print('While parado com Flag')
print('-'*30)
soma = res = count = 0
while res != 999:
    res = int(input('Digite um valor ( 999 pra parar): '))
    if res == 999:
        break
    soma += res
    count += 1
print(f' A soma dos {count} valores e a soma deles é {soma:.2f}')
    


