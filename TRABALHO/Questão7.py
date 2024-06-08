# 7) Escreva um algoritmo que leia o nome do aluno, o nome da disciplina, 2 notas, calcule a média, e informe se está aprovado ou reprovado como na saída: {nome} está {situacao} na disciplina {disciplina}.

nm = input("Qual o nome do aluno ? ")
dis = input("Qual a disciplina desejada? ")
p = float(input("Digite a nota parcial: "))
b = float(input("Digite a nota bimestral: "))
m = (p + b)/2

if m >= 6:
    sit = "Aprovado"
else:
    sit = "Reprovado"

print("=" * 30)
print("O aluno {}, ficou {}, na disciplina de {}, com média {}".format(nm, sit, dis, m))
