# Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme
# exemplo. Em seguida, mostrar na tela somente os números negativos da matriz.
linhas = int(input("Qual a quantidade de linhas da matriz(máximo = 10)?"))
colunas = int(input("Qual a quantidade de colunas da matriz(máximo = 10)?"))
matriz = [[0 for x in range(colunas)]for x in range(linhas)]
qtdN = 0
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
print("VALORES NEGATIVOS: ")
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < 0:
            print(matriz[i][j])
            qtdN += 1
if qtdN == 0:
    print("Não há números negativos na matriz!")