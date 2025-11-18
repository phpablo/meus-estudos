# Universidade Federal do Cariri - UFCA
# Disciplina : Estrutura de Dados - Semestre 2025.2
# Pablo Henrique Lima de Araújo

# ATIVIDADE DO VETOR NÃO ORDENADO - EXCLUIR

# criei meu vetor
vetor = [5, 10, 15, 20, 25]
# mostrei na tela o vetor todo
print("Vetor inicial:", vetor)

# Removendo elemento escolhido pelo usuário
# peço pro usuario digitar o valor que ele deseja excluir que tem no vetor
# preciso converter esse valor pra inteiro usando o int
# pq tudo que o usuario inputa é considerado string, oq daria problema ao comparar com os valors do vetor
valor = int(input("Digite o valor que deseja excluir: "))

# aqui verifica se o valor existe dentro do vetor
if valor in vetor:
    # se existir, ele entra no vetor e remove o valor e dps mostra o vetor na tela
    # já sem o valor que foi removido
    vetor.remove(valor)
    print("Vetor após exclusão:", vetor)
# se o valor digitado não existir no vetor, ele mostra a mensagem na tela mostrando que não encontrou
# esse valor dentro do vetor
else:
    print("Valor não encontrado no vetor.")