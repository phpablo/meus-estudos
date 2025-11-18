n = int(input('Qual tamanho da lista :\n'))
ls = [0] * n
for i in range(0,n):
    ls[i] = int(input('Qual número inserir na lista?\n '))
for v in ls:
    print(v)
# for i in range(0,n): # acessa o valor da lista, não o índice
#    print( ls[i])
# for indice,valor in enumerate(ls): # mostra o índice e o valor
#    print(f"O valor da Lista no índice {indice} é {valor}")
