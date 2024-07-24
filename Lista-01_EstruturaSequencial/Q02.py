#Entrada de dados pelo usuário.

temperaturaC = float(input("Digite a temeperatura em graus Celsius: "))

#Conversão da temperatura em graus Celsius para graus Fahrenheit com base na fórmula.
#Impressão do resultado na tela do usuário.

temperaturaF = (temperaturaC * 1.8) + 32
print("{:.0f}".format(temperaturaC), "graus Celsius equivalem a", "{:.0f}".format(temperaturaF), "graus Fahrenheit.")

