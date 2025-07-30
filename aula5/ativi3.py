def preco_com_desconto(preco, desconto):
    valor_desconto = (preco * desconto) / 100
    final = preco - valor_desconto
    return round(final, 2)

p = float(input("Digite o preço do produto: "))
d = float(input("Digite o desconto (%): "))
print("Preço com desconto: R$", preco_com_desconto(p, d))

