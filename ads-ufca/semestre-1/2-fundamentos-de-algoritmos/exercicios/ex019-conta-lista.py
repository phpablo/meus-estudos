n = int(input("Digite um número inteiro positivo :\n"))
ls = [0]*n
for i in range(0,n):
    ls[i] = int(input("Digite o número inteiro no indice %d da lista\n" % i))
for i in range(0,n):
    if ls[i] == ls[n-1]:
        print(i)