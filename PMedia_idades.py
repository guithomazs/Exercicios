# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSÍVEL CALCULAR".
idade = int(input("Digite as idades: "))
idades: int = 0
cont = 0
while idade >= 0:
    idades += idade
    cont += 1
    idade = int(input())
if cont >= 1:
    idades = idades / cont
    print(f"A média das idades é de {idades:.2f} anos")
else:
    print("Impossível calcular!")