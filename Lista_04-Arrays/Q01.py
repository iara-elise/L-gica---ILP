listaNum = []
contadorPares = 0

print("Digite 10 números inteiros:")

for i in range(10):
    num = int(input())

    listaNum.append(num)

for num in listaNum:
    if num % 2 == 0 and num != 0:
        contadorPares += 1

print("A quantidade de números pares inseridos na lista é: ", contadorPares)