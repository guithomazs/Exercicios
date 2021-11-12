# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.
qtd = int(input("Quantos casos você vai digitar? "))
for i in range(0, qtd):
    num = float(input("Entre com o numerador: "))
    deno = float(input("Entre com o denominador: "))
    if deno == 0:
        print("DIVISÃO IMPOSSÍVEL!")
    else:
        divisao = num / deno
        print(f'Divisão = {divisao:.2f}')