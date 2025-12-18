from random import randint

NOME_DO_PROGRAMA = "Condicional - Ano bissexto"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
ano = int(input("Qual ano? "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')



















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










