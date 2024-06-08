# 10) Peça ao usuário para inserir um número e use um loop for para imprimir a tabuada da multiplicação desse número (de 1 a 10).

numero = int(input("Insira um número: "))

print(f"Tabuada de multiplicação de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
