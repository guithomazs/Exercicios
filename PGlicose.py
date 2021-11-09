# Fazer um programa para ler a quantidade de glicose
# no sangue de uma pessoa e depois mostrar na tela a
# classificação desta glicose de acordo com a tabela de
# referência ao lado. Normal até 100 // 100 < Elevado <= 140 // Diabetes > 140

medida = float(input("Digite a medida da glicose: "))
if medida <= 100:
    print("Classificação: Normal")
elif medida <= 140:
    print("Classificação: Elevado")
elif medida > 140:
    print("Classificação: Diabetes")