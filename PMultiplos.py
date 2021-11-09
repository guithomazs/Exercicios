# Fazer um programa para ler dois números inteiros, e dizer se um número
# é múltiplo do outro. Os números podem ser digitados em qualquer ordem.
print("Digite dois números inteiros: ")
a = int(input())
b = int(input())
if a % b == 0 or b % a == 0:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")