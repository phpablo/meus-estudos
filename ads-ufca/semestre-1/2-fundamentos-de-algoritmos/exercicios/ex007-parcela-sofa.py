print("================================\n")
print("CALCULADORA DE PARCELAS\n")
print("================================\n")

valor_vista = float(input("Qual preço total do sofá?"))
qtd_parcelas = int(input("\nQual total de parcelas ?"))
valor_parcela = (valor_vista * 0.01 * (1.01 ** qtd_parcelas)) / ((1.01 ** qtd_parcelas) - 1)
valor_prazo = valor_parcela * qtd_parcelas
print("O valor total do sofá é de R$ %.2f e o valor de cada parcela será R$ %.2f" % (valor_prazo,valor_parcela))


print("================================\n")
print("         FIM PROGRAMA           \n")
print("================================\n")