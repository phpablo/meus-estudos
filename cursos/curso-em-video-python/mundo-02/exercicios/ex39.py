from datetime import date

# Get the current year
ano_atual = date.today().year

# Get birth year
nasc = int(input('Digite seu ano de nascimento: '))

# Calculate Age (This was missing)
idade = ano_atual - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.")

if idade < 18:
    saldo = 18 - idade
    print("Ainda não tem 18 anos. Não pode se alistar.")
    print(f"Falta(m) {saldo} ano(s) para o alistamento.")
    print(f"Seu alistamento será em {ano_atual + saldo}.")

elif idade == 18:
    print("Você tem 18 anos. Deve se alistar IMEDIATAMENTE!")

elif idade > 18:
    saldo = idade - 18
    print(f"Você já passou da idade de alistamento.")
    print(f"Deveria ter se alistado há {saldo} ano(s).")
    print(f"Seu alistamento foi em {ano_atual - saldo}.")