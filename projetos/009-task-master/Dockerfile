# 1. A Base: Começamos com um sistema Linux leve que já tem Python 3.10 instalado
FROM python:3.10-slim

# 2. A Bancada: Definimos a pasta de trabalho dentro do container
WORKDIR /app

# 3. Os Ingredientes: Copiamos apenas a lista de dependências primeiro
# (Fazemos isso separado para o Docker aproveitar o cache se o código mudar, mas as libs não)
COPY requirements.txt .

# 4. O Preparo: Instalamos as dependências dentro do container
RUN pip install --no-cache-dir -r requirements.txt

# 5. O Recheio: Copiamos todo o resto do seu código para dentro do container
COPY . .

# 6. A Ação: O comando que roda quando o container liga
# host 0.0.0.0 é vital para o container aceitar conexões de fora dele
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]