from datetime import date
from src.models import Categoria, Receita, Despesa

try:
    # 1. Criar Categorias
    cat_salario = Categoria("Salário", "RECEITA")
    cat_lazer = Categoria("Lazer", "DESPESA", limite=500.0)

    # 2. Criar Lançamentos
    minha_receita = Receita(5000.0, cat_salario, date.today(), "Salário Mensal", "PIX")
    minha_despesa = Despesa(200.0, cat_lazer, date.today(), "Cinema", "Crédito")

    print("Sucesso!")
    print(minha_receita)
    print(minha_despesa)

    # 3. Testar erro (Descomente para testar)
    # despesa_ruim = Despesa(-100, cat_lazer, date.today(), "Erro", "Pix") # Deve dar erro

except Exception as e:
    print(f"Erro capturado: {e}")