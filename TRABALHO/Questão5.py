# 5) Leia um número inteiro entre 0 e 23, este valor representa a hora do relógio. Dada essa hora, informe se o horário é manhã, tarde ou noite
hr = int(input("Digite o horário: "))

if 0<= hr < 12:
    print("Está de manhã")
elif 12 <= hr < 18:
    print("Está a tarde")
else:
    print("Está a noite")