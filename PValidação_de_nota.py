# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente1
x1 = float(input("Digite a primeira nota: "))
while not 0 <= x1 <= 10:
    x1 = float(input("Valor invalido! Tente novamente: "))
x2 = float(input("Digite a segunda nota: "))
while not 0 <= x2 <= 10:
    x2 = float(input("Valor invalido! Tente novamente: "))
media = (x1 + x2) / 2
print(f'MÉDIA = {media:.2f}')