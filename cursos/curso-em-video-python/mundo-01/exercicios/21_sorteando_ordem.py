import random
NOME_DO_PROGRAMA = "Sorteando um Aluno para apresentação"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
alunos = []

while len(alunos) < 4:
    aluno = input(f'>>> Digite o nome do {len(alunos)+1}º aluno: ')
    alunos.append(aluno)
    print("-" * 30)

print('\n... Sorteando ...\n')


print(f'\n\n{"="*10} RESULTADO DO SORTEIO {"="*10}')
print(f'>>> Lista de Alunos: {alunos}')
print("="*40)
for i in range(len(alunos)):
    aluno_escolhido = random.choice(alunos)
    print(f'>>> Apresentação {i+1}: {aluno_escolhido.upper()}')
    alunos.remove(aluno_escolhido)




















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










