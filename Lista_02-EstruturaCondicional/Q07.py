valor_01 = int(input("Valor 01:"))
valor_02 = int(input("Valor 02:"))
valor_03 = int(input("Valor 03:"))

c_ou_d = input("\nDeseja ver os valores em ordem crescente ou decrescente? ")

if c_ou_d == 'Crescente':

    if valor_01 < valor_02 and valor_01 < valor_03 and valor_02 < valor_03:
     print(f"{valor_01}, {valor_02}, {valor_03}")

    elif valor_02 < valor_01 and valor_02 < valor_03 and valor_03 < valor_01:
     print(f"{valor_02}, {valor_03}, {valor_01}")

    else:
     print(f"{valor_03}, {valor_02}, {valor_01}")

elif c_ou_d == 'Descrescente':
  
  if valor_01 > valor_02 and valor_01 > valor_03 and valor_02 > valor_03:
    print(f"{valor_01}, {valor_02}, {valor_03}")

  elif valor_02 > valor_01 and valor_02 > valor_03 and valor_03 > valor_01:
    print(f"{valor_02}, {valor_03}, {valor_01}")

  else:
    print(f"{valor_03}, {valor_02}, {valor_01}")

#REVER QUESTÃO