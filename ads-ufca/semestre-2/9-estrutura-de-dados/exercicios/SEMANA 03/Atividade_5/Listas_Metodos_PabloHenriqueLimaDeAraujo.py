# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

#  1 - Lista ligada simples (Classe Nó):

import numpy as np

class No: # crio uma classe
    def __init__(self,valor): # construtor da classe
        self.valor = valor # recebe o valor especifico que é passado ao ser instanciado
        self.proximo = None # ponteiro para o proximo elemento [ se inicia nulo ]

    # funcao mostrar nó
    def mostrar_no(self):
        print(self.valor) # mostrar o valor

# 2 -  Lista ligada simples (Classe Lista encadeada):
class Lista_encadeada: # cria a classe de lista encadeada
    def __init__(self): # o construtor nao vai receber nenhum parâmetro
        self.primeiroLista = None # vai apontar para o primeiro elemento da lista [ começa nulo ]

    # 3 -  Lista ligada simples (Inserir): métodos de inserir elemento no inicio da lista
    def inserir_inicio(self,valor): # crio o metodo que  vai inserir
        novo = No(valor) # varivavel que vai receber o nó [ elemento ]
        novo.proximo = self.primeiroLista # recebe  o ponteiro
        self.primeiroLista = novo # aponta para o novo objeto

    # funcao mostrar
    def mostrar(self): # mostrar o valor o promimo elemento
        atual = self.primeiroLista # variavel atual para receber o primeiro elemento
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo # atual vai receber o proprio atual mais o próximo

    # 4 - Lista ligada simples (Excluir):
    # funcao excluir
    def excluir_inicio_lista(self): # apaga o elemento
        if self.primeiroLista.proximo == None: # verifica que se ja tiver null, ela ta vazia
            print("Lista vazia")
            return None

        temporaria = self.primeiroLista # recebe o primeiro da lista

        self.primeiroLista = self.primeiroLista.proximo # recebendo ela mesma e o proximo é como se pulasse o elemento
        return temporaria

    # 5 -  Lista ligada simples (Pesquisar):
    # funcao pesquisar
    def pesquisar(self,valor): # crio metodo de pesquisar
        if self.primeiroLista == None: # faço uma verificação se for none retorna uma mensagem de que ta vazia
            print("Lista vazia")
            return None

        atual = self.primeiroLista # recebo o primeiro da lista
        while atual.valor != valor: # loop de verificação
            if atual.proximo == None: # se for None, return None pq ta vazia
                return None
            else: atual = atual.proximo # o atual recebe o atual
            return atual # retorna o atual