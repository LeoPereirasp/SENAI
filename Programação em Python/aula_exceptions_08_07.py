# try: Tentativa de realizar algo.
# except: Executar mediante um erro genérico ou específico.
# finally: Sempre será executado.
a = 10
b = "10"
try:
    print(a + b)
except TypeError:
    print("Só podemos somr números")
finally:
    print("Gostaria de executar mai uma operação?")

# Exemplo com mais tipos de erros
a = 10
b = 0

try:
    print(a / b)
except TypeError:
    print("Só podemos realizar divisões entre números, não str.")
except ZeroDivisionError:
    print("Divisão por zero é indeterminação matemática.")
finally:
    print("Nova operação?")

import requests
from uuid import uuid4

def busca_cep(cep: str) -> str:
    cep = cep.replace("-", "")
    req = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    try:
        return req.json()["city"]
    except Exception as e:
        raise ValueError(f"esse CEP não existe, favor revisar: {e}.")
    finally:
        print("O número da entrega é:")
        print("N: ", uuid4())

print(busca_cep("01001000"))
print(busca_cep("01001000625723"))

def le_arquivo(nome: str) -> str:
    try:
        with open (f"{nome}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Esse arquivo não existe."

print(le_arquivo("dados"))
print(le_arquivo("codigos"))
