# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

class OperacaoVetor:
    def __init__(self):
        self.vetor = []

    def valores(self):
        for i in range(10):
            num = int(input(f"Digite o {i+1}º número: "))
            self.vetor.append(num)

    def maior(self, valor_ref):
        return [n for n in self.vetor if n > valor_ref]

    def conta_menor(self, valor_ref):
        return sum(1 for n in self.vetor if n < valor_ref)

    def conta_repetir(self, valor_ref):
        return self.vetor.count(valor_ref)

v = OperacaoVetor()
v.valores()

valor_ref = int(input("Digite o valor de referência: "))

print("\nA) Maiores que o valor referência:", v.maior(valor_ref))
print("B) Quantos são menores:", v.conta_menor(valor_ref))
print("C) Quantas vezes aparece:", v.conta_repetir(valor_ref))

