# Parâmetros Especiais:
def soma(*args):
    """
    Soma vários números
    :param args: números int ou float
    :return: a soma de todos os args
    """
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6, 7))

def media(*args):
    """
    Calcula a média de args
    :param args: números int ou float
    :return: a média de args
    """
    from statistics import mean
    return mean(args)

print(media(1, 2, 3, 4, 5, 6, 7))

def padroniza_nome(*args: str) -> str:
    """
    Padroniza os nomes para persistir no DB.
    :param args: nomes do usuário
    :return: retorna o nome no padrão Nome Sobrenome1 Sobrenome2 ...
    """
    return " ".join([n.title() if len(n) > 3 else n.lower() for n in args])

print(padroniza_nome("thiago", "franciso", "andrade", "de", "lima"))

# **kwargs -> Keyword Args
from typing import Dict, List
from pandas import DataFrame
def lista_telefonica(**kwargs) -> DataFrame:
    """
    Gerar uma lista telefônica
    :param kwargs: nome: telefone
    :return: um dicionário como lista telefônica
    """
    data = {"Nomes": list(kwargs.keys()),
            "Telefones": list(kwargs.values())}
    return DataFrame(data=data)
print(lista_telefonica(thiago=1, maria=2, daniel=3, ana=4))

# Exemplo Estoque kwargs
def add_produtos( estoque: Dict, **kwargs) -> None:
    """
    Atualiza o estoque, add produtos
    :param estoque: estoque
    :param kwargs: produtos e quantidades
    :return: None
    """
    estoque.update(kwargs)
estoque = {"macarrão": 10}
add_produtos(estoque=estoque, tomate=20, cebola=30)
print(estoque)




