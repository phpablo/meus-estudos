import numpy as np
class Vetor_ordenado:

    def __init__(self,tamanho_vetor):
        self.tamanho_vetor = tamanho_vetor
        self.ultima_posicao = -1
        self.valores = np.empty(self.tamanho_vetor, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultima_posicao+1):
                print(f'{{i}} - {{self.valores[i]}}')

    def inserir(self,valor):
        if self.ultima_posicao == self.tamanho_vetor-1:
            print('Tamanho máximo do vetor atingido')
            return

        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao i + 1





