# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior
# distância que conseguir. Você deve criar um programa para, dadas as medidas das
# três tentativas de lançamento, informar qual foi a maior.
print("Digite as tres distancias:")
a = float(input())
b = float(input())
c = float(input())
if a >= b and a >= c:
    print(f"Maior distância: {a:.2f}")
elif b >= a and b >= c:
    print(f"Maior distância: {b:.2f}")
elif c >= a and c >= b:
    print(f"Maior distância: {c:.2f}")