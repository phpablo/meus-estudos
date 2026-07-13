# ETL PDF Extractor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/your-username/etl-pdf-extractor/pulls)

Um script Python simples e eficiente para extrair dados de tabelas em arquivos PDF e exportar para Excel, com foco em filtrar clientes por cidades específicas.

## 📋 Descrição

Este projeto automatiza o processo de Extração, Transformação e Carregamento (ETL) de dados de PDFs contendo tabelas de clientes. O script lê um arquivo PDF, identifica linhas de tabelas que correspondem a cidades alvo, extrai informações relevantes (nome, telefone, email) e salva os dados em um arquivo Excel.

Ideal para processamento de listas de clientes, relatórios ou qualquer documento PDF tabular.

## ✨ Funcionalidades

- **Extração Inteligente**: Utiliza `pdfplumber` para extrair tabelas de PDFs com alta precisão.
- **Filtragem por Cidade**: Busca automática por cidades específicas, ignorando acentos e maiúsculas/minúsculas.
- **Progresso Visual**: Barra de progresso com `tqdm` para acompanhar o processamento das páginas.
- **Exportação para Excel**: Salva os dados extraídos em formato Excel usando `pandas`.
- **Tratamento de Erros**: Segurança contra linhas incompletas ou dados ausentes.
- **Configurável**: Índices das colunas facilmente ajustáveis para diferentes layouts de tabela.

## 🛠️ Requisitos

- Python 3.8 ou superior
- Bibliotecas Python:
  - `pdfplumber`
  - `pandas`
  - `unidecode`
  - `tqdm`

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/your-username/etl-pdf-extractor.git
   cd etl-pdf-extractor
   ```

2. **Instale as dependências:**
   ```bash
   pip install pdfplumber pandas unidecode tqdm
   ```

   Ou, se preferir usar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🚀 Uso

1. **Prepare seu PDF:**
   - Coloque o arquivo PDF na pasta do projeto (por padrão: `list.pdf`).
   - Certifique-se de que o PDF contenha tabelas com dados de clientes.

2. **Configure o script:**
   - Edite as variáveis no início do `extrator_pdf.py`:
     - `arquivo_pdf`: Caminho para o arquivo PDF de entrada.
     - `arquivo_excel_saida`: Nome do arquivo Excel de saída.
     - `cidades_alvo`: Lista de cidades para filtrar.
     - `IDX_NOME`, `IDX_CIDADE`, `IDX_TELEFONE`, `IDX_EMAIL`: Índices das colunas na tabela.

3. **Execute o script:**
   ```bash
   python extrator_pdf.py
   ```

4. **Verifique o resultado:**
   - O arquivo Excel será gerado na pasta do projeto.
   - Abra o arquivo para visualizar os dados extraídos.

## ⚙️ Configuração

### Índices das Colunas

Ajuste os índices conforme o layout da sua tabela PDF:

```python
IDX_NOME = 2        # Coluna do nome
IDX_CIDADE = 12     # Coluna da cidade
IDX_TELEFONE = 17   # Coluna do telefone
IDX_EMAIL = 9       # Coluna do email
```

### Cidades Alvo

Modifique a lista de cidades para filtrar:

```python
cidades_alvo = ['santo antonio', 'aguas lindas', 'outra cidade']
```

## 📊 Exemplo de Saída

O script gera um arquivo Excel com as seguintes colunas:

| Nome          | Telefone     | Email               | Cidade Encontrada |
|---------------|--------------|---------------------|-------------------|
| João Silva    | (11) 9999-8888 | joao@email.com     | Santo Antônio    |
| Maria Santos  | (21) 8888-7777 | maria@email.com    | Águas Lindas     |

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [pdfplumber](https://github.com/jsvine/pdfplumber) - Para extração de tabelas de PDF
- [pandas](https://pandas.pydata.org/) - Para manipulação de dados
- [tqdm](https://github.com/tqdm/tqdm) - Para barras de progresso
- [unidecode](https://pypi.org/project/Unidecode/) - Para normalização de texto

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!