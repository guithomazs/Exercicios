# Uma lanchonete possui vários produtos. Cada produto possui um código
# e um preço. Você deve fazer um programa para ler o código e a
# quantidade comprada de um produto (suponha um código válido), e daí
# informar qual o valor a ser pago, com duas casas decimais, conforme
# tabela de produtos ao lado.
# 1 = R$ 5.00 // 2 = R$ 3.50 // 3 = R$ 4.80 // 4 = R$ 8.90 // 5 = R$ 7.32

precos: float = [0 for i in range(5)]
precos[0] = 5.00
precos[1] = 3.50
precos[2] = 4.80
precos[3] = 8.90
precos[4] = 7.32
cod = int(input("Código do produto comprado: "))
qtd = int(input("Quantidade comprada: "))
valor = qtd * precos[cod-1]
print(f"Valor a pagar: R$ {valor:.2f}")