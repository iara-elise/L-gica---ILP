saida = ""
soma = 0

qtdNum = int(input("Quantos números você quer somar? "))

for i in range(qtdNum):
    num = int(input())

    soma += num

    for i in range(num):
        saida = num, "+" 

print(saida)
