# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0 (zero)
qtd = int(input("Quantos números você vai digitar? "))
vetor = [0]*qtd
maior_valor: float = 0
maior_pos: int = 0
for i in range(0, qtd):
    vetor[i] = float(input("Digite um número: "))
for i in range(0, qtd):
    for j in range(0, qtd):
        if vetor[j] > vetor[i] and vetor[j] > maior_valor:
            maior_valor = vetor[j]
            maior_pos = j
print("Maior valor = {:.1f}".format(maior_valor))
print("Maior posição = {:d}".format(maior_pos))