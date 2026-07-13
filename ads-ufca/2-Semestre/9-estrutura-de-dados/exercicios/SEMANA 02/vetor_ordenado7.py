vetor = [ 1,2,3,4,5,6,7,8,9]
numero = 11
encontrado = False
for elemento in vetor:
    if elemento == numero:
        encontrado = True
        break
    elif elemento > numero:
        break

if encontrado:
    print(f'O numero {numero} foi encontrado')
else:
    print(f'O numero {numero} não existe no vetor')