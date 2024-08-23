# PARTE 1
# Declarando listas vazias.  

listaNum = []
novaLista = []

# PARTE 2
# A variável "qtdNum" armazena a quantidade de itens que o usuário deseja guardar na lista.

qtdNum = int(input("Quantos números você deseja inserir? \n"))

# PARTE 3
# O for percorre a quantidade de números inseridos pelo usuário para declarar os itens da lista através da variável "num". A entrada é dada pelo usuário. Após a entrada de dados, a função "append" adiciona "num" a "listaNum".

for i in range(qtdNum):
    num = int(input())

    listaNum.append(num)

# PARTE 4
# O for utiliza a variável "num" para percorrer a "listaNum".
# Dentro do for, há uma condicional com a seguinte condição: se "num" não existir em "novaLista", "num" será adicionado à "novaLista", ou seja, ela verifica se há números repetidos e se houver, eles não serão adicionados à "novaLista".
# Ao final do programa, a "novaLista" é impressa sem números repetidos.

for num in listaNum:
    if num not in novaLista:
        novaLista.append(num)

print(novaLista)