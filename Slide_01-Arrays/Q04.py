# PARTE 1
# Declarando lista vazia.  

listaNum = []

# PARTE 2
# A variável "qtdNum" armazena a quantidade de itens que o usuário deseja guardar na lista.

qtdNum= int(input("Quantos números você deseja inserir? \n"))

# PARTE 3
# O for percorre a quantidade de números inseridos pelo usuário para declarar os itens da lista através da variável "num". A entrada é dada pelo usuário. Após a entrada de dados, a função "append" adiciona "num" a "listaNum".

for i in range(qtdNum):
    num = int(input())

    listaNum.append(num)

# PARTE 4
# Utilizando list comprehension, a variável "i" é elevada ao quadrado, em seguida o laço for percorre "listaNum", uma condicional verifica se o valor armazenado em "i" é impar. Por fim, "novaLista" é impressa.

novaLista = [i ** 2 for i in listaNum if i % 2 != 0]

print(novaLista)

