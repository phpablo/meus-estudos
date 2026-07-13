def merge_sort(lista):
    # Se a lista tiver apenas um elemento ou estiver vazia,
    # ela já está ordenada
    if len(lista) <= 1:
        return lista

    # Encontra o ponto médio da lista
    meio = len(lista) // 2

    # Divide a lista em duas partes
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    # Intercala as duas listas ordenadas
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Enquanto houver elementos em ambas as listas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


# Exemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(lista))