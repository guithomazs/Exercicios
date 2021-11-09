# Fazer um programa para ler as medidas da base e altura de um retângulo.
# Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo,
# com quatro casas decimais

from math import sqrt

base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do terreno: "))
area = base * altura
perimetro = base*2 + altura*2
diagonal = sqrt(base**2 + altura**2)
print(f"Área = {area:.4f}")
print(f"Perímetro = {perimetro:.4f}")
print(f"Diagonal = {diagonal:.4f}")
