# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens.
qtd = int(input("Quantas pessoas serão digitadas? "))
vetAltura: float = [0]*qtd
qtdH = 0
qtdM = 0
mediaM = 0
maior_altura = 0
menor_altura = 0
for i in range(0, qtd):
    vetAltura[i] = float(input(f'Altura da {i+1}ª pessoa: '))
    gen = input(f"Gênero da {i+1}ª pessoa(M/F): ")
    if gen.lower() == 'm':
        qtdH += 1
    else:
        qtdM += 1
        mediaM += vetAltura[i]

mediaM = mediaM / qtdM
menor_altura = vetAltura[0]

for i in range(0, qtd):
    for j in range(0, qtd):
        if vetAltura[j] > vetAltura[i] and vetAltura[j] > maior_altura:
            maior_altura = vetAltura[j]
        if vetAltura[j] < vetAltura[i] and vetAltura[j] < menor_altura:
            menor_altura = vetAltura[j]
print(f'Menor altura = {menor_altura}')
print(f'Maior altura = {maior_altura}')
print(f'Media das alturas das mulheres = {mediaM:.2f}')
print('Número de homens = {:d}'.format(qtdH))