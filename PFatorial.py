# Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
# fatorial de N.
N = int(input("Digite um valor NATURAL para N(máximo 15): "))
fatorial = N
for i in range(N, 0, -1):
    if i == N:
        continue
    fatorial = fatorial * i
    if N == 0:
        fatorial = 1
print(f'Fatorial = {fatorial}')