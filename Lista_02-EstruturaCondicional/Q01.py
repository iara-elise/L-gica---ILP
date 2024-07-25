# Entrada de dados pelo usuário.

salario = float(input("Digite o seu salário: "))

if salario <= 1903.98:
    print("Você está isento do imposto de renda!")

elif salario <= 2826.65:
    impostoDeRenda = salario * 7.5 / 100
    print(f"Total de imposto a pagar: R$ {impostoDeRenda:.1f}")

elif salario <= 3751.05:
    impostoDeRenda = salario * 15 / 100
    print(f"Total de imposto a pagar: R$ {impostoDeRenda:.1f}")

elif salario <= 4664.68:
    impostoDeRenda = salario * 22.5 / 100
    print(f"Total de imposto a pagar: R$ {impostoDeRenda:.1f}")

else:
    impostoDeRenda = salario * 27.5 / 100
    print(f"Total de imposto a pagar: R$ {impostoDeRenda:.1f}")

    
