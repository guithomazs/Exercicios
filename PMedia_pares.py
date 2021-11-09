# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NUMERO PAR"
qtd = int(input("Quantos elementos vai ter o vetor? "))
qtd1: int = 0
vet = [0]*qtd
media: float = 0
for i in range(0, qtd):
    vet[i] = int(input("Digite um número: "))
    if vet[i] % 2 == 0:
        media += vet[i]
        qtd1 += 1
media = media / qtd1
if media == 0:
    print("NENHUM NÚMERO PAR!")
else:
    print("MÉDIA DOS PARES = {:.1f} ".format(media))