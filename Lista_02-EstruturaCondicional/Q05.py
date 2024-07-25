#Entrada de dados pelo usuário.

valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))

#A condição verifica se valor_01 é maior que valor_2.

#Se valor_01 for maior que valor_02, a variável diferenca irá armazenar a subtração entre valor_01 e valor_02.
#Em seguida, será impressa uma mensagem informando a difereça do maior número para o menor.

#Se não, a variável diferenca irá armazenar a substração entre valor_02 e valor_01.
##Em seguida, será impressa uma mensagem informando a difereça do maior número para o menor.

if valor_01 > valor_02:
    diferenca = valor_01 - valor_02
    print(f"\nA diferença entre {valor_01} e {valor_02} é {diferenca}")

else:
    diferenca = valor_02 - valor_01
    print(f"\nA diferença entre {valor_02} e {valor_01} é {diferenca}")
