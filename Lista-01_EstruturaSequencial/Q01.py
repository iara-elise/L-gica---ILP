print("CALCULADORA \n")

#Entrada de dados por parte do usuário.

valor_01 = float(input("Digite o valor 01: "))
valor_02 = float(input("Digite o valor 02: "))

#Calculando as quatro operações básicas:

#SOMA:

soma = valor_01 + valor_02
print("\nO resultado da soma entre os valores digitados é", "{:.1f}".format(soma), "\n")

#SUBTRAÇÃO

subtracao = valor_01 - valor_02
print("O resultado da subtração entre os valores digitados é", "{:.1f}".format(subtracao), "\n")

#MULTIPLICAÇÃO

mutiplicacao = valor_01 * valor_02
print("O resultado da multiplicação entre os valores digitados é", "{:.1f}".format(mutiplicacao), "\n")

#DIVISÃO

divisao = valor_01 / valor_02
print("O resultado da divisão entre os valores digitados é", "{:.1f}".format(divisao))