# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit
# ou vice-versa. Para isso, você deve construir um programa que leia a letra "C" ou "F"
# indicando em qual escala vai ser informada uma temperatura. Em seguida o programa
# deve mostrar a temperatura na outra escala com duas casas decimais.
c: float = 0
f: float = 0
temp = input("Voce vai digitar a temperatura em qual escala (C/F)? ")
if str.lower(temp) == 'c':
    c = float(input("Digite a temperatura em Celsius: "))
    f = c * 9/5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {f:.2f}")
elif str.lower(temp) == 'f':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = 5/9 * (f - 32)
    print(f"Temperatura equivalente em Celsius: {c:.2f}")