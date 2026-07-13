class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = []

    # Método privado para verificar o tamanho atual
    def __tamanho(self):
        return len(self.dados)

    # Método privado para verificar se a pilha está cheia
    def __pilha_cheia(self):
        return self.__tamanho() == self.capacidade

    # Método privado para verificar se a pilha está vazia
    def __pilha_vazia(self):
        return self.__tamanho() == 0

    # Métodos públicos para empilhar e desempilhar
    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("❌ A pilha está cheia. Não é possível empilhar.")
        else:
            self.dados.append(valor)
            print(f"✅ Valor {valor} empilhado com sucesso!")

    def desempilhar(self):
        if self.__pilha_vazia():
            print("⚠️ A pilha está vazia. Não é possível desempilhar.")
        else:
            valor = self.dados.pop()
            print(f"🔹 Valor {valor} removido do topo.")

# Exemplo de uso
p = Pilha(3)
p.empilhar(10)
p.empilhar(20)
p.empilhar(30)
p.empilhar(40)  # Tentativa além da capacidade
p.desempilhar()