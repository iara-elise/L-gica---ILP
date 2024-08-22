listaNum = []
listaPares = []


qtdNum = int(input("Quantos números você deseja inserir? \n"))

for i in range(qtdNum):
    num = int(input())

    listaNum.append(num)

numAlvo = int(input("Insira o número alvo: "))

for num_01 in listaNum:
    for num_02 in listaNum:
        if num_01 + num_02 == numAlvo:
            if [num_01, num_02] not in listaPares and [num_02, num_01] not in listaPares:
                listaPares.append([num_01, num_02])

print(listaPares)

# Vai pra casa do caralho