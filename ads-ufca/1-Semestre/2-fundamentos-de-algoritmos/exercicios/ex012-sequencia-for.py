print("SEQUENCIA DE 3 NUMEROS NEGATIVOS")
print("================================")



n = int(input('\nDigite um número inteiro:'))

for i in range(0, n+1):
    for j in range (0, n+1):
        for k in range(0, n+1):
            if i + j + k == n:
                print("%d + %d + %d = %d" % (i,j,k,n))















print("================================")
print("         FIM PROGRAMA           ")