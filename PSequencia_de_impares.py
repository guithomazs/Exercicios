# Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
# se for o caso.
x = int(input("Digite um número inteiro: "))
if x % 2 != 0:
    x += 1
for i in range(0, x):
    if i % 2 != 0:
        print(i)