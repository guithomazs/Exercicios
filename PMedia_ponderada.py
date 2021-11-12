# Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
# teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
# que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
# que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
# pela soma dos pesos.
peso1 = 2
peso2 = 3
peso3 = 5
qtd = int(input("Quantos casos você vai digitar? "))
for i in range(0, qtd):
    print("Digite 3 números: ")
    a = float(input())
    b = float(input())
    c = float(input())
    media = ((a*peso1) + (b*peso2) + (c*peso3)) / (peso1 + peso2 + peso3)
    print(f'Média = {media:.1f}')