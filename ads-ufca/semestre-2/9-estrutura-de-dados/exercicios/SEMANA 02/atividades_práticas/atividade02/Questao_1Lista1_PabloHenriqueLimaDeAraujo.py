# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

class MediaVetor:
    def __init__(self,vetor):
        self.vetor = vetor

    def calcula_media(self):
        if len(self.vetor) == 0:
            return 0
        return sum(self.vetor) / len(self.vetor)

v1 = [7,1,6,2]
v_media = MediaVetor(v1)
print(f'A média é ', v_media.calcula_media())
