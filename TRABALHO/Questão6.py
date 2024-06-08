# 6) Sabendo que a idade mínima para um cidadão estar apto a votar é de 16 anos. Escreva um algoritmo que lê o nome do cidadão, sua idade e informa se ele pode emitir o seu título de eleitor ou não

nm = input("Digite o seu nome: ")
idd = int(input("Digite a sua idade: "))

if idd >= 16:
    print("{}, com {} anos você está apto a tirar o título !".format(nm, idd))
else:
    print("Você não pode tirar o título")