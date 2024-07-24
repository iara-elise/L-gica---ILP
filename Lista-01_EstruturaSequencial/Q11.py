#Entrada de dados pelo usuário.

segundos = int(input("Digite a quantidade de segundos: "))

#A variável "horas" armazena a divisão dos segundos inseridos pelo usuário por 3600 (total de segundos presentes em 1h).
horas = segundos / 3600

#A variável "segundosRestantes" armazena o resto da divisão entre os segundos inseridos pelo usuário e 3600.
segundosRestantes = segundos % 3600

#A variável "minutos" armazena a divisão entre a variável "segundosRestantes" e 60 (total de segundos presentes em 1 minuto).
minutos = segundosRestantes / 60

#A variável "segundos" armazena o resto da divisão entre a variável "segundosRestantes" e 60.
segundos = segundosRestantes % 60

#Impressão do resultado na tela do usuário.

print(f"Os segundos inseridos dão ---> {horas:.0f}h:{minutos:.0f}:{segundos:.0f}")

