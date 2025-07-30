def gorjeta(conta, porcentagem):
    return (conta * porcentagem) / 100

total = float(input("Digite o valor da conta: "))
taxa = float(input("Digite a porcentagem da gorjeta: "))
print("Valor da gorjeta é:", gorjeta(total, taxa))
