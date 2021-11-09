# Fazer um programa para ler uma duração de tempo em segundos, daí
# imprimir na tela esta duração no formato horas:minutos:segundos.
segs: int = 0
minutos: int = 0
horas: int = 0
segs = int(input("Digite a duração em segundos: "))
while segs >= 60:
    segs -= 60
    minutos += 1
    if minutos >= 60:
        minutos -= 60
        horas += 1
print(f"{horas}:{minutos}:{segs}")