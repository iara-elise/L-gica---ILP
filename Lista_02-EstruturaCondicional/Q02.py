ano = int(input("Digite um ano:"))

if ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto.")
else:
    print("É não.")