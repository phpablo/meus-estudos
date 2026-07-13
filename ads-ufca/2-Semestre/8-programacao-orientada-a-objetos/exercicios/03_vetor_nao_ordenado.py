import numpy as np
class VetorNaoOrdenado:
    def __init__(self,tamanho_vetor):
        self.tamanho_vetor = tamanho_vetor
        self.ultima_posicao = -1
        self.valores = np.empty(self.tamanho_vetor, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('Vetor Vazio')
        else:
            for i in range(self.ultima_posicao +1):
                print(i,' - ', self.valores[i])

    def inserir(self,valor):
        if self.ultima_posicao == self.tamanho_vetor -1:
            print("Tamanho máximo do vetor atingido")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
               return i
        return -1
    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[ i + 1 ]
            self.ultima_posicao -= 1


v1 = VetorNaoOrdenado(4)
v1.inserir(2)
v1.inserir(7)
v1.inserir(9)
v1.inserir(4)

v1.excluir(2)
v1.imprimir()





# vetor = [3,4,7]
# print(f'Vetor inicial: ', vetor)
# vetor.append(2)
# print(f'Vetor com um elemento na ultima posição: ',vetor)
# vetor.insert(0,99)
# print(f'Vetor com elemento inserido no meio: ', vetor)


