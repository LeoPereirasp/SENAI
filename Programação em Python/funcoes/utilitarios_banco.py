from random import randint
def gera_conta() -> str:
    return f"{randint(100, 999)}-{randint(0,9)}"