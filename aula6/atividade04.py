import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave in dados:
        info = dados[chave]
        print("Cotação Atual:", info["bid"])
        print("Máximo:", info["high"])
        print("Mínimo:", info["low"])
        print("Data:", info["create_date"])
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar cotação.")
