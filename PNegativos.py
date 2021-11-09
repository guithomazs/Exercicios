# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos
qtd = int(input("Quantos números você vai digitar? "))
vetor = [0 for i in range(qtd)]
for i in range(0, qtd):
    vetor[i] = float(input("Digite um número: "))

print("NÚMEROS NEGATIVOS:")
for i in range(0, qtd):
    if (vetor[i]) < 0:
        print(vetor[i])