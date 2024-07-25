# Entrada de dados pelo usuário.

num = float(input("Digite um número entre 1 e 10: "))

# A condição verifica se o número inserido pelo usuário é menor ou igual a 10.

# Se o número for menor ou igual a 10, o programa exibirá uma mensagem informando que o valor digitado está dentro do intervalo.
# Se não, será exibido uma mensagem informando que o número digitado está fora do intervalo solicitado.

if num <= 10:
    print("O número digitado está dentro da faixa solicitada!")

else:
    print("O número digitado está fora da faixa solicitada!")