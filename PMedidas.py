# Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar
# (imprimir os dados com quatro casas decimais):
# a) a área do quadrado que tem lado A
# b) a área do triângulo retângulo que base A e altura B
# c) a área do trapézio que tem bases A e B, e altura C

a = float(input("Digite a medida de A: "))
b = float(input("Digite a medida de B: "))
c = float(input("Digite a medida de C: "))
print(f"ÁREA DO QUADRADO = {a*a:.4f}")
print(f"ÁREA DO TRIÂNGULO = {a*b/2:.4f}")
print(f"ÁREA DO TRAPÉZIO = {(a+b)*c / 2:.4f}")