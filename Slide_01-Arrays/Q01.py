listaNum = []
novaLista = []


qtdNum = int(input("Quantos números você deseja inserir? \n"))

for i in range(qtdNum):
    num = int(input())

    listaNum.append(num)

for num in listaNum:
    if num not in novaLista:
        novaLista.append(num)

print(novaLista)