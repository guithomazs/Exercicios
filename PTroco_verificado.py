# Fazer um programa para calcular o troco no processo de pagamento de um produto de
# uma mercearia. O programa deve ler o preço unitário do produto, a quantidade de
# unidades compradas deste produto, e o valor em dinheiro dado pelo cliente. Seu
# programa deve mostrar o valor do troco a ser devolvido ao cliente. Se o dinheiro dado
# pelo cliente não for suficiente, mostrar uma mensagem informando o valor restante
preco = float(input("Preço unitário do produto: "))
qtd = int(input("Quantidade comprada do produto: "))
din_receb = float(input("Dinheiro recebido: "))
preco = preco * qtd
if preco > din_receb:
    print(f"Dinheiro insuficiente, faltam {preco - din_receb:.2f} reais")
else:
    print(f"Troco = {din_receb - preco:.2f} R$")