tabuada = 0

num = int(input("Digite um número entre 1 e 10: "))

for i in range(10):
    tabuada = (i + 1) * num
    
    print(num, " * ", i + 1, "=", tabuada)