# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10.
x = int(input("Digite um número inteiro: "))
for i in range (1, 11):
    print(f"{x} X {i} = {x * i}")