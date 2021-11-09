# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
# mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.
qtd = int(input("Quantos elementos vai ter o vetor? "))
vet = [0]*qtd
media: float = 0
for i in range(0, qtd):
    vet[i] = float(input("Digite um número: "))
    media += vet[i]
media = media / qtd
print("")
print('MÉDIA DO VETOR = {:f}'.format(media))
print('ELEMENTOS ABAIXO DA MÉDIA: ')
for i in range(0, qtd):
    if vet[i] < media:
        print(vet[i])