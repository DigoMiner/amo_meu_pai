# Solicita as informações do aluno
nome = input("Digite o nome do aluno: ")
ra = input("Digite o Registro Acadêmico (RA) do aluno: ")

# Solicita as notas dos bimestres
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica o resultado
if media >= 6:
    resultado = "Aprovado"
elif media >= 4.5 and media < 6:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

# Imprime o resultado
print(f"Aluno: {nome} (RA: {ra})")
print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")