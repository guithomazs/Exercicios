# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
# mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
# programa deve finalizar quando forem digitados dois valores iguais.
X = int(input("Digite dois números inteiros: "))
Y = int(input())

while X != Y:
    if X < Y:
        print("Crescente!")
    elif X > Y:
        print("Decrescente!")

    X = int(input("Digite outros dois números inteiros: "))
    Y = int(input())
print("Números iguais digitados, encerrando!")