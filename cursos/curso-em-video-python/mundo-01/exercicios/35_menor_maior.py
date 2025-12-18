from random import randint

from pandas.compat.numpy import np_version_gte1p24

NOME_DO_PROGRAMA = "Condicional - menor_maior"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
# encontra o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#encontra o maior
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor é o número {menor}')
print(f'O maior é o número {maior}')




















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










