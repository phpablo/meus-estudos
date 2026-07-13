n = int(input('Digite o tamanho da lista que seja maior ou igual a 2:\n'))
ls = [0]*n
for i in range(0,n):
    ls[i] = int(input('Digite o inteiro no indice %d da lista\n' % i))
acum = 0
for i in range(0, n-1):
    for j in range(i+1,n):
        if ls[i] > ls[j]:
            acum += 1
print(acum)

