# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo
qtd = int(input("Quantos números você vai digitar? "))
dentro: int = 0
fora: int = 0
for i in range (0, qtd):
    num = float(input("Digite um número: "))
    if 10 <= num <= 20:
        dentro += 1
    else:
        fora += 1
print(f'Dentro = {dentro}')
print(f'Fora = {fora}')