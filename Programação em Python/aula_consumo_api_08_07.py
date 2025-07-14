import requests
from typing import Dict

def busca_cep(cep: str) -> Dict:
    cep = cep.replace("-", "")
    req = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    return req.json()
print(busca_cep("01001000"))