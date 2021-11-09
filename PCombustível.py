# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
# 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
# 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
# código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
# como as quantidades de cada combustível.
cod = input("Informe um código (1, 2, 3) ou 4 para parar: ")
alco = 0
gaso = 0
dies = 0
while True:
    cod = int(cod)
    if cod == 1:
        alco += 1
    elif cod == 2:
        gaso += 1
    elif cod == 3:
        dies += 1
    elif cod == 4:
        break
    elif cod > 4 or cod < 1:
        cod = input("Por favor digite um número no intervalo correto(1,2,3) ou 4 para parar: ")
        continue
    cod = input("Informe um código (1, 2, 3) ou 4 para parar: ")
print(f'Álcool(1) = {alco}')
print(f'Gasolina(2) = {gaso}')
print(f'Diesel(3) = {dies}')