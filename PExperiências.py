# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto.
qtd = int(input("Quantos casos de teste serão digitados? "))
total_cobaias: int = 0
coelho: int = 0
rato: int = 0
sapo: int = 0
for i in range (0, qtd):
    qtd1 = int(input("Quantidade de cobaias: "))
    total_cobaias += qtd1
    tipo = input("Tipo de cobaia(C/R/S): ")
    if tipo.lower() == 'c':
        coelho += qtd1
    elif tipo.lower() == 'r':
        rato += qtd1
    elif tipo.lower() == 's':
        sapo += qtd1
porcentCoelho = coelho * 100 / total_cobaias
porcentSapo = sapo * 100 / total_cobaias
porcentRato = rato * 100 / total_cobaias

print("RELATÓRIO FINAL:")
print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {porcentCoelho:.2f}%')
print(f'Percentual de ratos: {porcentRato:.2f}%')
print(f'Percentual de sapos: {porcentSapo:.2f}%')