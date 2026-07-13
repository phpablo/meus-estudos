from pandas.io.formats.format import return_docstring

NOME_DO_PROGRAMA = "Manipulando texto - Frase"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
frase = str(input("Frase: "))
qtd = frase.upper().count("A")
print(f'Letra A se repete {qtd} vezes')

print('A letra A aparece pela primeira vez na posição:',frase.upper().find("A"))
print('A letra A aparece pela ultima vez na posição:',frase.upper().rfind("A"))


















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










