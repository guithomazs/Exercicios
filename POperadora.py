# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a
# 100 minutos de telefone. Cada minuto que exceder a franquia de 100 minutos custa
# R$ 2.00. Fazer um programa para ler a quantidade de minutos que uma pessoa consumiu,
# daí mostrar o valor a ser pago.
excesso: int = 0
minutos = int(input("Digite a quantidade de minutos: "))
if minutos > 100:
    excesso = minutos - 100
    excesso = excesso * 2
print(f"Valor a pagar: R$ {50 + excesso:.2f}")
