# Leia os valores das coordenadas X e Y de um ponto no plano
# cartesiano. A seguir, determine qual o quadrante ao qual pertence o
# ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a
# mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva
# “Eixo X” ou “Eixo Y”, conforme for a situação.
x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
if (x > 0) and (y > 0):
    print("Quadrante 1")
elif (x < 0) and (y > 0):
    print("Quadrante 2")
elif (x < 0) and (y < 0):
    print("Quadrante 3")
elif (x > 0) and (y < 0):
    print("Quadrante 4")
elif x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo X")
elif y == 0:
    print("Eixo Y")