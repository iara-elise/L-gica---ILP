soma = 0

print("Digite 5 números: ")

for i in range(5):
    num = int(input())

    if num % 2 == 0:
        soma += num

print("A soma dos números pares digitados é: ", soma)