# Fazer um programa para ler as medidas da largura e comprimento de um terreno
# retangular com uma casa decimal, bem como o valor do metro quadrado do terreno
# com duas casas decimais. Em seguida, o programa deve mostrar o valor da área
# do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais.

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do terreno: "))
print(f"o tamanho da área é de {largura * comprimento:.2f} metros.")
print(f"O valor da área do terreno é de {largura * comprimento * valor:.2f}.")
