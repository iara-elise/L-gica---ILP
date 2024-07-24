#Entrada de dados pelo usuário.

altura = float(input("Digite a altura do triângulo: "))
base = float(input("Digite a base do triângulo: "))

#Calculando a base do triângulo com base na fórmula.
#Impressão do resultado na tela do usuário.

areaTriangulo = altura * base / 2
print("\nA área do triângulo é", "{:.1f}".format(areaTriangulo))