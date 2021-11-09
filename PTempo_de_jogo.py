# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração
# mínima de 1 hora e máxima de 24 horas.
import re
hora_inicial = input("Que horas começou o jogo?(0-23):")
hora_final = input("Que horas acabou o jogo?(0-23):")

hora_inicial = re.findall(r"\d+", hora_inicial)
hora_final = re.findall(r"\d+", hora_final)
hinicial = int(hora_inicial[0])
hfinal = int(hora_final[0])

if 0 <= hinicial <=23 and 0<= hfinal <= 23:

    if hinicial < hfinal:
        tempo = (hfinal - hinicial)
        print(f'Tempo de jogo: {tempo} horas')

    elif hinicial == hfinal:
        tempo = 24
        print(f'Tempo de jogo: {tempo} horas')

    elif hinicial > hfinal:
        tempo = 24 - (hinicial - hfinal)
        print(f'Tempo de jogo: {tempo} horas')
else:
    print("Por favor insira os horários entre 0 e 23!")