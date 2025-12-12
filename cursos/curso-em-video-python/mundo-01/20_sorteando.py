import random
NOME_DO_PROGRAMA = "Sorteando um Aluno"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
alunos = []

while len(alunos) < 4:
    aluno = input(f'>>> Digite o nome do {len(alunos)+1}º aluno: ')
    alunos.append(aluno)
    print("-" * 30)

print('\n... Sorteando ...\n')
aluno_escolhido = random.choice(alunos)

print(f'\n\n{"="*10} RESULTADO DO SORTEIO {"="*10}')
print(f'>>> Lista de Alunos: {alunos}')
print("="*40)
print(f'>>> O ALUNO ESCOLHIDO FOI: {aluno_escolhido.upper()}')




















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










