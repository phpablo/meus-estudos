# Aqui está um exemplo minimalista de como gravar dados estruturados (binários) em um arquivo, simulando o que seria enviado por um socket:

import struct

# 1. Dados que queremos salvar
id_usuario = 101
pontuacao = 95.5

# 2. Empacotando: '>' (Big-endian/Rede), 'I' (Unsigned Int), 'f' (Float)
# Resolve o problema de comunicação entre sistemas diferentes [12, 13]
dados_binarios = struct.pack('>If', id_usuario, pontuacao)

# 3. Gravando de forma segura usando 'with' [7]
with open('dados.bin', 'wb') as f: # 'wb' = write binary
    f.write(dados_binarios)
    
print(f"Dados empacotados: {dados_binarios}")