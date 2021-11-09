# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares.
qtd = int(input("Quantos números voce vai digitar? "))
vetor = [0]*qtd
qtdpares: int = 0
for i in range(0, qtd):
    vetor[i] = float(input("Digite um numero: "))
print("NÚMEROS PARES: ")
for i in range(0, qtd):
    if vetor[i] % 2 == 0:
        print(vetor[i], end='  ')
        qtdpares += 1
print("")
print("Quantidade de pares = {:d} ".format(qtdpares))