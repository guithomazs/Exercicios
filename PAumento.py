# Uma empresa vai conceder um aumento percentual de
# salário aos seus funcionários dependendo de quanto
# cada pessoa ganha, conforme tabela ao lado. Fazer um
# programa para ler o salário de uma pessoa, daí mostrar
# qual o novo salário desta pessoa depois do aumento,
# quanto foi o aumento e qual foi a porcentagem de
# aumento. até R$ 1000,00 = 20% // acima de R$1000 até 3000 = 15% //
# acima de R$ 3000,00 até 8000 = 10% // acima de R$8000,00 = 5%

salario = float(input("Digite o salário da pessoa: "))
if salario <= 1000:
    porcent = 20
    aumento = salario * porcent / 100
    salario = salario + aumento

elif salario <= 3000:
    porcent = 15
    aumento = salario * porcent / 100
    salario = salario + aumento

elif salario <= 8000:
    porcent = 10
    aumento = salario * porcent / 100
    salario = salario + aumento

elif salario > 8000:
    porcent = 5
    aumento = salario * porcent / 100
    salario = salario + aumento
print(f'Novo salário = R$ {salario:.2f}')
print(f'Aumento = R$ {aumento:.2f}')
print(f'Porcentagem = {porcent} %')