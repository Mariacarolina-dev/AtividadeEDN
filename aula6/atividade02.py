import requests

url = "https://randomuser.me/api/"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    pessoa = dados['results'][0]

    nome = f"{pessoa['name']['first']} {pessoa['name']['last']}"
    email = pessoa['email']
    pais = pessoa['location']['country']

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)
else:
    print("Erro ao buscar perfil.")
