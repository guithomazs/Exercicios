# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento
# de cada linha. Suponha não haver empates.
ordem = int(input("Qual a ordem da matriz(máximo = 10)? "))
matriz = [[0 for x in range(ordem)]for x in range(ordem)]
maior: float = 0
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
print("MAIOR ELEMENTO DE CADA LINHA: ")
for i in range(ordem):
    print(f'Linha {i+1}: ', end='')
    for j in range(ordem):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(maior)
    maior = 0