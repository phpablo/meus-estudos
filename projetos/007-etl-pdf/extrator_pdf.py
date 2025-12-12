import pdfplumber
import pandas as pd
from unidecode import unidecode
from tqdm import tqdm

# --- CONFIGURAÇÕES ---
arquivo_pdf = 'list.pdf'
arquivo_excel_saida = 'Relatorio_Final.xlsx'

cidades_alvo = ['santo antonio', 'aguas lindas']


IDX_NOME = 2
IDX_CIDADE = 12
IDX_TELEFONE = 17
IDX_EMAIL = 9

dados_extraidos = []

print("--- INICIANDO O ROBÔ ---")

with pdfplumber.open(arquivo_pdf) as pdf:
    # 2. A MÁGICA ACONTECE AQUI NA LINHA DE BAIXO vvv
    # tqdm(pdf.pages) cria a barra de progresso automática baseada no total de páginas
    for pagina in tqdm(pdf.pages, desc="Lendo Páginas", unit="pág"):

        tabela = pagina.extract_table()

        if tabela:
            for linha in tabela:
                # Segurança para não quebrar se a linha for curta
                if not linha or len(linha) <= IDX_CIDADE:
                    continue

                cidade_no_pdf = linha[IDX_CIDADE] or ""
                cidade_limpa = unidecode(cidade_no_pdf).lower()

                # Lógica de busca
                encontrou = False
                for alvo in cidades_alvo:
                    if alvo in cidade_limpa:
                        encontrou = True
                        break

                if encontrou:
                    # Captura os dados com segurança
                    nome = linha[IDX_NOME] if len(linha) > IDX_NOME else ""
                    telefone = linha[IDX_TELEFONE] if len(linha) > IDX_TELEFONE else ""
                    email = linha[IDX_EMAIL] if len(linha) > IDX_EMAIL else ""

                    novo_cliente = {
                        'Nome': nome,
                        'Telefone': telefone,
                        'Email': email,
                        'Cidade Encontrada': cidade_no_pdf
                    }
                    dados_extraidos.append(novo_cliente)

print(f"\n Processo finalizado!")
print(f"Total de clientes encontrados: {len(dados_extraidos)}")

if dados_extraidos:
    print("Salvando Excel... aguarde.")
    df = pd.DataFrame(dados_extraidos)
    df.to_excel(arquivo_excel_saida, index=False)
    print(f"✅ Sucesso! Abra o arquivo '{arquivo_excel_saida}'")
else:
    print("⚠️ Nenhum dado encontrado. Verifique os índices das colunas.")