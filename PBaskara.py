# Fazer um programa para ler os três coeficientes de uma equação do segundo grau.
# Usando a fórmula de Baskara, calcular e mostrar os valores das raízes x1 e x2
# da equação com quatro casas decimais, conforme exemplo. Se a equação não possuir
# raízes reais, mostrar uma mensagem.
from math import sqrt
a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))
delta = (b*b) +(-4)*a*c
if delta > 0:
    print(f"x1 = {(-(b) - sqrt(delta)) / (2*a):.4f}")
    print(f"x2 = {(-(b) + sqrt(delta)) / (2*a):.4f}")
elif delta == 0:
    print(f"x1 = {(-b - delta) / (2 * a):.4f}")
else:
    print("Essa equação não possui raízes reais")