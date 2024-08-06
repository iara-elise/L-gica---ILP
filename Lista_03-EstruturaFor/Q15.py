contadorImpar = 0
contadorPar = 0

num = float(input("Digite os números: \n"))

while num > 0:
    num = float(input())

    if num % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1

print("Quantidade de números ímpares: ", contadorImpar)
print("Quantidade de números pares: ", contadorPar)
