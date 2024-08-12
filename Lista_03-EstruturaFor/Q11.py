saida = ""
soma = 0

qtdNum = int(input("Quantos números você quer somar? "))

print("Digite os números:")

for i in range(qtdNum):
    num = int(input())

    if i > 0:
        saida += "+"

    saida += str(num)
    soma += num

saida += "=" + str(soma)
print(saida)
    
