# Manipulando Arquivos
# TXT
# 1 - FORMA
file = open("teste.txt", "w")
file.write("Arquivo de Teste")
file.close()

file = open("teste.txt", "r")
print(file.read())
file.close()

# 2 - FORMA
with open("teste.txt", "a") as file:
    file.write("\nLinha2")

with open("teste.txt", "r") as file:
    print(file.readlines())

dados = {}

with open("dados.txt", "r") as file:
    for _ in file.readlines():
        line = _.replace("\n", "").replace(" ", "")
        # chave = line.split(":")[0]
        # valor = line.split(":")[1]
        chave, valor = line.split(":")
        dados[chave] = valor

print(dados)

# JSON - dados semi-estruturados
import json
from uuid import uuid4

dados = {
    str(uuid4()):{
        "nome": "Leonardo",
        "sobrenome": "Pereira",
        "email": "leonardogonpereira@gmail.com"
    }
}

with open("dados.json", "w") as file:
    json.dump(dados, file)

with open("dados.json") as file:
    print(json.load(file))

# Exemplo com API
import requests
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
req = requests.get(url)
print(req.json()["USDBRL"]["high"])

def consulta_alta_moeda(moeda: str) -> None:
    url = f"https://economia.awesomeapi.com.br/last/{moeda.upper()}-BRL"
    req = requests.get(url)
    print("R$" + req.json()[f"{moeda.upper()}BRL"]["high"])
consulta_alta_moeda("usd")
consulta_alta_moeda("eur")
consulta_alta_moeda("btc")