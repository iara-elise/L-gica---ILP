listaNum = []

qtdNum= int(input("Quantos números você deseja inserir? \n"))

for i in range(qtdNum):
    num = int(input())

    listaNum.append(num)

novaLista = [i ** 2 for i in listaNum if i % 2 != 0]

print(novaLista)

