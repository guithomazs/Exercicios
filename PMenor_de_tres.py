# Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o
# menor dentre os três números lidos. Em caso de empate, mostrar apenas uma vez.

a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))
if a <= b and a <= c:
    print(f"Menor = {a}")
elif b <= a and b <= c:
    print(f"Menor = {b}")
elif c <= a and c <= b:
    print(f"Menor = {c}")