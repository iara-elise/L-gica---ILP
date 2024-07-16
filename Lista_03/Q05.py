soma = 0

print("Digite 5 números: \n")

for i in range(5):
    num = int(input())

    if num < 10 :
        soma += num

print("A soma dos números abaixo de 10 é: ", soma)