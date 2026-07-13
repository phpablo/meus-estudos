# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

#  Fila circular (Enfileirar):

import numpy as np

class Fila_circular:
    def __init__(self,tamanho_vetor):
        self.tamanho_vetor = tamanho_vetor # valor recebido
        self.final = -1 # mostra que está vazio ou final da fila
        self.inicio = 0
        self.numero_de_elementos = 0 # inicializa zerado
        self.valores = np.empty(self.tamanho_vetor, dtype=int) # cria um vetor vazio mas com tamanho definido no contrutor

    def __fila_vazia(self):
        return self.numero_de_elementos == 0 # ve se ta vazia

    def __fila_cheia(self):
        return self.numero_de_elementos == self.tamanho_vetor # ve se ta cheia

    # função enfileirar
    def enfileirar(self,valor): # funcao para enfileirar
        if self.__fila_cheia(): # verifica se esta cheia e retorna uma mensagem confirmando
            print('A fila está cheia')
            return
        if self.final == self.tamanho_vetor -1: # verifica se o indice final atingiu o final do vetor
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor  # insere na posicao correspondente
        self.numero_de_elementos += 1 # ultimo que entrou na fila

    # função desenfileirar - remove um elemento no inicio da fila
    def desenfileirar(self):
        if self.__fila_vazia(): # verifica se vazia, retorna uma mensagem
            print('A fila se encontra vazia')
            return

        temporaria = self.valores[self.inicio]  # guarda o primeiro elemento
        self.inicio +=1 # aponta pro proximo da fila
        if self.inicio == self.tamanho_vetor: # verifica se chegou ao final do vetor
            self.inicio = 0
            self.numero_de_elementos -= 1
            return temporaria

    # funcao primeiro elemento da fila - mostra o element do inicio da fila
    def primeiro_fila(self):
        if self.__fila_vazia():
            print('A fila se encontra vazia')
            return -1
        return self.valores[self.inicio]

fila = [3,4,7,5,99]
fila.append(22)
fila.pop()
fila.remove(4)
print(fila[0])

from collections import deque

# fila com 3 elementos
fila2 = deque(['amarelo','azul','branco'])

# adicionar elementos
fila2.append("Vermelha")
print("Adicionar cor :", fila2)

# remover elemento
fila2.popleft()
print("Remover um elemento :", fila2)


