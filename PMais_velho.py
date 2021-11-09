# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha
qtd = int(input("Quantas pessoas você vai digitar? "))
vetorNome = ['']*qtd
vetorIdade = [0]*qtd
mais_velho: int = 0
for i in range(0, qtd):
    print(f'Dados da {i+1}ª pessoa: ')
    vetorNome[i] = input("Nome: ")
    vetorIdade[i] = int(input("Idade: "))
for i in range(0, qtd):
    for j in range(0, qtd):
        if vetorIdade[j] > vetorIdade[i] and vetorIdade[j] > mais_velho:
            mais_velho = vetorIdade[j]
            pos = j
print('PESSOA MAIS VELHA: {:s}'.format(vetorNome[pos]))