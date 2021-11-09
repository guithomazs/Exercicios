# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor
qtd = int(input("Quantos números voce vai digitar? "))
vetor = [0] * qtd
soma: float = 0
for i in range(0, qtd):
    vetor[i] = float(input("Digite um número: "))
    soma += vetor[i]
media = soma / qtd

print(f'Soma = {soma}')
print(f'Média = {media}')