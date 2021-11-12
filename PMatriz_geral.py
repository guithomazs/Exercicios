# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
# seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada.
ordem = int(input("Qual a ordem da matriz(máximo = 10)? "))
matriz = [[0 for x in range(ordem)]for x in range(ordem)]
soma = 0

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
        if matriz[i][j] > 0:
            soma += matriz[i][j]

print("")
print(f"Soma dos positivos: {soma}")
print("")
x = int(input("Escolha uma linha: "))
print("LINHA ESCOLHIDA = ", end='')
for i in range(x, x+1):
    for j in range(ordem):
        print(matriz[i][j], end='  ')

print("")
print("")
x = int(input("Escolha uma coluna: "))
print("COLUNA ESCOLHIDA = ", end='')
for i in range(ordem):
    for j in range(x, x+1):
        print(matriz[i][j], end='  ')

print("")
print("")
print("DIAGONAL PRINCIPAL: ", end='')
for i in range(ordem):
    for j in range(ordem):
        if i == j:
            print(matriz[i][j], end='  ')

print("")
print("")
print("MATRIZ ALTERADA: ")
for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] < 0:
            matriz[i][j] = matriz[i][j] ** 2
        print(matriz[i][j], end='  ')
    print("")