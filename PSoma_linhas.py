# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz
# de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor
# seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado.
linhas = int(input('Qual a quantidade de linhas da matriz? '))
colunas = int(input('Qual a quantidade de colunas da matriz? '))
matriz: [[float]] = [[0 for x in range(colunas)]for x in range(linhas)]
soma_linha = 0
for i in range(linhas):
    print(f'Digite os elementos da {i+1}ª linha: ')
    for j in range(colunas):
        matriz[i][j] = float(input())
print("Vetor gerado: ")
for i in range(linhas):
    for j in range(colunas):
        soma_linha += matriz[i][j]
    print(soma_linha)
    soma_linha = 0