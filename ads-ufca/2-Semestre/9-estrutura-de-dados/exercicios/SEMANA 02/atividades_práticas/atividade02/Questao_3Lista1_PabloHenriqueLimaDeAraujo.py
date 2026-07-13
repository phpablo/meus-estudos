# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, valor):
        self.itens.append(valor)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        return None

    def vazia(self):
        return len(self.itens) == 0

    def mostrar(self):
        print(self.itens)

    def ordenar(self):
        pilha_aux = []

        while not self.vazia():
            temp = self.pop()

            while pilha_aux and  pilha_aux[-1]> temp:
                self.push(pilha_aux.pop())

            pilha_aux.append(temp)

        self.itens = pilha_aux

p = Pilha()
p.push(5)
p.push(1)
p.push(3)
p.push(4)
p.push(2)

print("Pilha original:")
p.mostrar()

p.ordenar()

print("\nPilha ordenada:")
p.mostrar()


