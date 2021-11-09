# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
# o vetor C gerado.
qtd = int(input("Quantos elementos vai ter cada vetor? "))
vetA = [0]*qtd
vetB = [0]*qtd
vetC = [0]*qtd
print("Digite os valores do vetor A: ")
for i in range(0, qtd):
    vetA[i] = float(input())
print("Digite os valores do vetor B: ")
for i in range(0, qtd):
    vetB[i] = float(input())
    vetC[i] = vetA[i] + vetB[i]
print("VETOR RESULTANTE: ")
for i in range(0, qtd):
    print(vetC[i])