#Entrada de dados pelo usuário.

print("NOTAS \n")

nota_01 = float(input("Nota 01: "))
nota_02 = float(input("Nota 02: "))
nota_03 = float(input("Nota 03: "))
nota_04 = float(input("Nota 04: "))

print("\nPESOS: \n")

peso_01 = int(input("Peso 01: "))
peso_02 = int(input("Peso 02: "))
peso_03 = int(input("Peso 03: "))
peso_04 = int(input("Peso 04: "))

#A variável somaDosPesos está armazenando a soma dos pesos inseridos pelo usuário anteriormente.
#A váriável mediaPonderada calcula a média ponderada utilizando as notas e os pesos inseridos pelo usuários anteriormente.

somaDosPesos = peso_01 + peso_02 + peso_03 + peso_04
mediaPonderada = (nota_01 * peso_01 + nota_02 + peso_02 + nota_03 * peso_03 + nota_04 * peso_04) / somaDosPesos

#Impressão do resultado na tela do usuário.

print(f"\nMÉDIA PONDERADA: {mediaPonderada:.1f}")