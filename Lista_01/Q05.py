#Declaração da variáve constante PI.

PI = float(3.14)

#Entrada de dados pelo usuário.

raio = float(input("Digite o valor do raio da esfera: "))

#Calculando o volume da esfera com base na fórmula.
#Impressão do resultado na tela do usuário.

volumeEsfera = 4 / 3 * PI * raio ** 3
print("O volume da esfera é", "{:.1f}".format(volumeEsfera))