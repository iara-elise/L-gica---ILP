somadorImpar = 0
somadorPar = 0

print("Digite 10 números: ")
for i in range(10):
    num = int(input())

    if num % 2 != 0:
        somadorImpar += num
    
    else:
        somadorPar += num

if somadorImpar > somadorPar:
    print("O somatório dos valores ímpares é maior.")
elif somadorPar > somadorImpar:
    print("O somatório dos valores ímpares é menor que o somatório dos números pares.")
else:
    print("O somatório é igual.")
