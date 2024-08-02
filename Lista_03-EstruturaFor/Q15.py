contadorImpar = 0
contadorPar = 0

num = float(input("Digite os números:"))

while num > 0:
    num = float(input())

if num % 2 != 0:
    contadorImpar += 1
else:
    contadorPar += 1

print("Quantidade de números ímpares: ", contadorImpar)
print("Quantidade de números pares: ", contadorPar)

#REVISAR