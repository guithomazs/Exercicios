# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
# cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
# dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada
linhas = int(input("Qual a quantidade de linhas de cada matriz(máximo = 10)?"))
colunas = int(input("Qual a quantidade de colunas de cada matriz(máximo = 10)?"))
matrizA = [[0 for x in range(colunas)]for x in range(linhas)]
matrizB = [[0 for x in range(colunas)]for x in range(linhas)]
print("Digite os valores da matriz A: ")
for i in range(linhas):
    for j in range(colunas):
        matrizA[i][j] = float(input(f'Elemento [{i},{j}]: '))
print("Digite os valores da matriz B: ")
for i in range(linhas):
    for j in range(colunas):
        matrizB[i][j] = float(input(f'Elemento [{i},{j}]: '))
print("MATRIZ SOMA: ")
for i in range(linhas):
    for j in range(colunas):
        print(matrizA[i][j] + matrizB[i][j], end='  ')
    print("")