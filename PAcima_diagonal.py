# Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Mostrar a soma dos elementos acima da
# diagonal principal. Um exemplo de números acima da diagonal
# principal é mostrado ao lado (no caso as células com fundo cinza).
ordem = int(input("Qual a ordem da matriz(máximo = 10)? "))
matriz = [[0 for x in range(ordem)]for x in range(ordem)]
soma = 0
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
for i in range(ordem):
    for j in range(ordem):
        if j > i:
            soma += matriz[i][j]
print("SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {:.1f}".format(soma))