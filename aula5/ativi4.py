from datetime import datetime

def dias_vivo(nasc):
    data_nasc = datetime.strptime(nasc, "%d/%m/%Y")
    hoje = datetime.today()
    dias = (hoje - data_nasc).days
    return dias

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
print("Você está vivo há", dias_vivo(nascimento), "dias.")



