# Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores
# negativos da matriz.
qtd = int(input("Qual a ordem da matriz? "))
matriz = [[0 for x in range(qtd)]for x in range(qtd)]
qtdNegativos: int = 0
for i in range(0, qtd):
    for j in range(0, qtd):
        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
print("DIAGONAL PRINCIPAL: ")
for i in range(0, qtd):
    for j in range(0, qtd):
        if i == j:
            print(matriz[i][j], end='  ')
        if matriz[i][j] < 0:
            qtdNegativos += 1
print("")
print(f"Quantidade de negativos: {qtdNegativos}")