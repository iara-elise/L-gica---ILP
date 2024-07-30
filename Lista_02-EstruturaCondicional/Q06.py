# Entrada de dados pelo usário.

valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))
valor_03 = int(input("Valor 03: "))

# BLOCO 1:
# A condição verifica se valor_01 é maior que valor_02 e valor_03. Em seguida ela verifica se valor_02 é maior que valor_03.
# Com base na verificação anterior, os valores serão impressão em ordem crescente.

# BLOCO 2:
# Se a primeiro condição for falsa, um segundo bloco será verificado.
# A condição verifica se valor_02 é maior que valor_01 e valor_03. Em seguida ela verifica se valor_03 é maior que valor_01.
# Com base na verificação anterior, os valores serão impressão em ordem crescente.

# BLOCO 3:
# Se o segundo bloco também for falso, o último bloco será executado.
# Será impresso na tela do usuário os números em ordem crescente. (Rever explicação posterirmente.)

if valor_01 < valor_02 and valor_01 < valor_03 and valor_02 < valor_03:
    print(f"{valor_01}, {valor_02}, {valor_03}")

elif valor_02 < valor_01 and valor_02 < valor_03 and valor_03 < valor_01:
    print(f"{valor_02}, {valor_03}, {valor_01}")

else:
    print(f"{valor_03}, {valor_02}, {valor_01}")


#REVER QUESTÃO