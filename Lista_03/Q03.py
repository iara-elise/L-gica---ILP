print("Digite dois valores de intervalo: \n")
valor_01 = int(input())
valor_02 = int(input())

soma = 0

for i in range (valor_01, valor_02 + 1):
    print(i)
    soma+=i
    print(soma)

