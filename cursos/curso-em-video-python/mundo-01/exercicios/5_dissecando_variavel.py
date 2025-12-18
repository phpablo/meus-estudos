from unicodedata import numeric

print('Desafio 5 - Dissecando Variável\n')
algo = input('Digite um numero ai : ')
print(f'O tipo primitivo desse valor é ', type(algo))
# tem so epaço
print(f'Só tem espaços : ', algo.isspace())
# e um numeric
print(f'É um número : ',algo.isnumeric())
# e alfabetico
print(f'É alfabético : ', algo.isalpha())
# e alfanumerico
print(f'É alfanumerico : ', algo.isalnum())
# esta maiusculo
print(f'É maiúsculo : ', algo.isupper())
# esta em minusculas
print(f'É maiúsculo : ', algo.islower())
# esta capitalizada
print(f'Está captalizada : ', algo.istitle())
