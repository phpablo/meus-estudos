n = int(input('Digite o tamanho da matriz quadrada:\n'))
mt = [0]*n
for i in range(0,n):
    mt[i] = [0]*n
    for j in range(0,n):
        mt[i][j] = int(input("Digite o valor (%d,%d) da matriz:" % (i,j)))
sao_iguais = True
for i in range(0,n):
    if mt[i][i] != mt[i][n-1 - i]:
        sao_iguais = False
        break
if sao_iguais:
    print("As diagonais da matriz são iguais")
else:
    print("As diagonais da matriz NÃO são iguais")