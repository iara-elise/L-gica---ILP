#Entrada de dados por parte do usuário.

valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))
valor_03 = int(input("Valor_03: "))

# A primeira condicional verifica se os valores inseridos anteriormente têm o necessário para formar um triângulo.
# Se sim, um segundo bloco será executado para descobrir qual tipo de triângulo será formado.
# Se não, uma mensagem informando que não é possível formar um triângulo será impressa na tela.

if valor_01 + valor_02 > valor_03 and valor_01 + valor_03 > valor_02 and valor_02 + valor_03 > valor_01:
    print("É possível formar um triângulo.")

    if valor_01 == valor_02 and valor_02 == valor_03:
        print("O triângulo é equilátero!")

    elif valor_01 == valor_02 or valor_01 == valor_03 or valor_02 == valor_03:
        print("O triângulo é isosceles!")

    else:
        print("O triângulo é escaleno!")

else:
    print("Não é possível formar um triângulo.")
