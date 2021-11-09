# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis).
qtd = int(input("Quantos alunos serão digitados? "))
vetNome = ['']*qtd
vetN1 = [0]*qtd
vetN2 = [0]*qtd
vetMedia = [0]*qtd
for i in range(0, qtd):
    print(f"Digite nome, primeira e segunda nota do {i+1}º aluno:")
    vetNome[i] = input("Nome: ")
    vetN1[i] = float(input("Nota 1: "))
    vetN2[i] = float(input("Nota 2: "))
    vetMedia[i] = (vetN1[i] + vetN2[i]) / 2
print("")
print("Alunos aprovados: ")
for i in range(0, qtd):
    if vetMedia[i] >= 6:
        print(vetNome[i])