#Entrada de dados pelo usuário.

print("EQUAÇÃO DE SEGUNDO GRAU \n")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = float(input("Digite o valor de x: "))

#A variável y armazena uma equação quadrática do tipo ax2 + bx + c. Os valores foram inseridos pelo usuário anteriormente.
#Impressão do resultado na tela do usuário.

y = (a * x ** 2) + (b * x) + c
print("O valor de y é:", "{:.0f}".format(y))