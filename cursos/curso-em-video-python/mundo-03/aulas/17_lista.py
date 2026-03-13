# TUPLAS - Resumo Prático

# 1. Criando tuplas
tupla_vazia = ()
tupla_um_elemento = (1,)  # Nota: a vírgula é necessária
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mista = (1, "texto", 3.14, True)

# 2. Acessando elementos
print(tupla_numeros[0])      # Primeiro elemento
print(tupla_numeros[-1])     # Último elemento
print(tupla_numeros[1:3])    # Slice

# 3. Propriedades principais
print(len(tupla_numeros))           # Tamanho
print(3 in tupla_numeros)           # Verificar se existe
print(tupla_numeros.count(2))       # Contar ocorrências
print(tupla_numeros.index(3))       # Índice de um elemento

# 4. Tuplas são IMUTÁVEIS
# tupla_numeros[0] = 10  # Erro!

# 5. Desempacotamento
a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")

# 6. Iteração
for numero in tupla_numeros:
  print(numero)

# 7. Conversão
lista = list(tupla_numeros)
tupla_nova = tuple(lista)