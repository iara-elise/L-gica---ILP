num = int(input("Digite um número inteiro: "))

for i in range(1, num):
    print("*" * i)

for i in range(num, 0, -1):
    print("*" * i)