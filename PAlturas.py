# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver.
qtd = int(input("Quantas pessoas serão digitadas? "))
vetNome = ['']*qtd
vetIdade = [0]*qtd
vetAltura = [0]*qtd
qtd1: int = 0
media: float = 0
for i in range(0, qtd):
    print(f'Dados da {i+1}ª pessoa: ')
    vetNome[i] = input("Nome: ")
    vetIdade[i] = int(input("Idade: "))
    vetAltura[i] = float(input("Altura: "))
    if vetIdade[i] < 16:
        qtd1 += 1
    media += vetAltura[i]

print("")
media = media / qtd
porcent = float(qtd1) * 100 / qtd

print("Altura média = {:.2f}".format(media))
print("Pessoas com menos de 16 anos = {:.1f}%".format(porcent))
for i in range(0, qtd):
    if vetIdade[i] < 16:
        print(vetNome[i])