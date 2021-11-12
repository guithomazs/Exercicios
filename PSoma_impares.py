# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles.
print("Digite dois números inteiros: ")
a = int(input())
b = int(input())
soma: int = 0
if a > b:
    a, b = b, a
for i in range (a, b):
    if i % 2 != 0:
        soma = soma + i
print(f"Soma dos ímpares = {soma}")
