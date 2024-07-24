#Declaração da variável constante PI.

PI = float(3.14)

#Entrada de dados pelo usuário.

raio = float(input("Digite o valor do raio: "))

#Calculando a área do circulo com base na fórmula.
#Impressão do resultado na tela do usuário.

areaCirculo = PI * raio ** 2
print("O valor da área do circulo é", "{:.1f}".format(areaCirculo))

