# Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar
# o valor da área do círculo com três casas decimais. A fórmula da área do círculo é a
# seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟**2. Você pode usar o valor de 𝜋 fornecido pela biblioteca da
# sua linguagem de programação, ou então, se preferir, use diretamente o valor 3.14159.

raio = float(input("Digite o valor do raio do círculo: "))
print(f"ÁREA = {3.14159 * (raio**2):.3f}")