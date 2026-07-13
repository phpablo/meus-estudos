import  datetime
import random

ano = random.randint(1995, 2020)
idade = datetime.date.today().year - ano
print(f'{idade} anos')
if(idade <= 9):
    print("Categoria: MIRIM")
elif(idade <= 14):
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 25:
    print("Categoria: SENIOR")
else:
    print("Categoria: MASTER")

