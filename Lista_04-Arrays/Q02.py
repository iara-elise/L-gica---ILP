listaNum_01 = []
listaNum_02 = []

imparesLista_01 = 0
imparesLista_02 = 0
paresLista_01 = 0
paresLista_02 = 0


tamanhoListas = int(input("Insira o tamanho da sua lista: "))

print("Insira os itens da primeira lista: ")

for i in range(tamanhoListas):
    num_01 = int(input())

    listaNum_01.append(num_01)

print("Insira os itens da segunda lista: ")

for i in range(tamanhoListas):
    num_02 = int(input())

    listaNum_02.append(num_02)

for num in listaNum_01:

    if num % 2 != 0:
        imparesLista_01 += num

    else:
        paresLista_01 += num

for num in listaNum_02:

    if num % 2 != 0:
        imparesLista_02 += num
    else:
        paresLista_02 += num

print()

print("Somatório dos números ímpares - Lista 01: ", imparesLista_01)
print("Somatório dos números ímpares - Lista 02: ", imparesLista_02)


if imparesLista_01 > imparesLista_02:
    print("Lista impar 01 > Lista impar 02!")

elif imparesLista_02 > imparesLista_01:
    print("Lista impar 02 > Lista impar 01!!")

else:
    print("Lista impar 01 = Lista impar 02")

print()
    
print("Somatório dos números pares - Lista 01: ", paresLista_01)
print("Somatório dos números pares - Lista 02: ", paresLista_02)

if paresLista_01 > paresLista_02:
    print("Lista par 01 > Lista par 02")

elif paresLista_02 > paresLista_01:
    print("Lista par 02 > Lista par 01")

else:
    print("Lista par 1 = Lista par 2")
