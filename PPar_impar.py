# Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
# se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
# apenas NULO.
qtd = int(input("Quantos números você vai digitar? "))
for i in range(0, qtd):
    num = int(input("Digite um número inteiro: "))
    if num > 0 and num % 2 == 0:
        print("Par positivo!")
    elif num > 0 and num % 2 != 0:
        print("Impar positivo!")
    elif num < 0 and num % 2 != 0:
        print("Impar negativo!")
    elif num < 0 and num % 2 == 0:
        print("Par negativo!")
    else:
        print("Nulo!")