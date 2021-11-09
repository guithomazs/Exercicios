# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
# proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total.
qtd = int(input("Serão digitados dados de quantos produtos? "))
lucro1: int = 0
lucro2: int = 0
lucro3: int = 0
lucroTotal: float = 0
VVendaTotal: float = 0
VCompraTotal: float = 0
for i in range(0, qtd):
    print(f"Produto {i+1}:")
    nome = input("Nome: ")
    compra = float(input("Preço de compra: "))
    VCompraTotal += compra
    venda = float(input("Preço de venda: "))
    VVendaTotal += venda

    lucro = venda - compra
    lucroTotal += lucro

    if (lucro * 100 / compra) < 10:
        lucro1 += 1
    elif 10 <= (lucro * 100 / compra) <= 20:
        lucro2 += 1
    elif (lucro * 100 / venda) > 20:
        lucro3 += 1

print("")
print("RELATÓRIO: ")
print(f'Lucro abaixo de 10%: {lucro1}')
print(f'Lucro entre 10% e 20%: {lucro2}')
print(f'Lucro acima de 20%: {lucro3}')
print(f'Valor total de compra: R$ {VCompraTotal:.2f} ')
print(f'Valor total de venda: R$ {VVendaTotal:.2f} ')
print(f'Lucro total: R$ {lucroTotal:.2f} ')