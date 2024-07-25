#Entrada de de dados pelo usuário.

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

#A variável imc está armazenando o cálculo do imc que será relizado com os dados inseridos anteriormente pelo usuário.
#Impressão do resultado na tela do usuário.

imc = peso / altura ** 2
print("Seu IMC é", "{:.2f}".format(imc))