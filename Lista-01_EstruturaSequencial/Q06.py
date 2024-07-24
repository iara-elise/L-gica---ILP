#Entrada de dados pelo usuário.

nota_01 = float(input("Nota 01: "))
nota_02 = float(input("Nota 02: "))
nota_03 = float(input("Nota 03: "))

#Calculando a média aritmética com base na fórmula.
#Impressão do resultado na tela do usuário.

mediaAritmetica = (nota_01 + nota_02 + nota_03) / 3 

print("\nNOTAS DIGITADAS:", nota_01, nota_02, nota_02) #Rever posteriormente.
print("\nMÉDIA ARITMÉTICA:", "{:.1f}".format(mediaAritmetica))

