# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
# sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
# algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
# escrever mensagem alguma).
print("Digite os valores de X e Y:")
x = int(input())
y = int(input())
while x != 0 and y != 0:
    if (x > 0) and (y > 0):
        print("Quadrante 1")
    elif (x < 0) and (y > 0):
        print("Quadrante 2")
    elif (x < 0) and (y < 0):
        print("Quadrante 3")
    elif (x > 0) and (y < 0):
        print("Quadrante 4")
    print("Digite os valores de X e Y:")
    x = int(input())
    y = int(input())