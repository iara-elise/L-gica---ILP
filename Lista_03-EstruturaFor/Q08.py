contador = 0

qtdValores = int(input("Digite um numero: "))

for i in range(qtdValores):
    num = int(input("Digite um numero: "))

    if num % 2 == 0:
        contador += 1
print("quantidade de numeros pares: ", contador)