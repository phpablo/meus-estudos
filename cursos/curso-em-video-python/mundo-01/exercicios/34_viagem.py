from random import randint

NOME_DO_PROGRAMA = "Condicional - Viagem"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
km_viagem = int(input("Viagem de quantos kilometros ? "))
preco = km_viagem * 0.5 if km_viagem <= 200 else km_viagem * 0.45 # forma simplificada condicao inline
print(f'Sua viagem custará R$ {preco}')

'''preco_passagem_200 = 0.50
preco_passagem_longa = 0.45
if km_viagem <=200:
    print(f'Sua viagem custará R$ {km_viagem*preco_passagem_200}')
else:
    print(f'Sua viagem custará R$ {km_viagem*preco_passagem_longa}')'''



















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










