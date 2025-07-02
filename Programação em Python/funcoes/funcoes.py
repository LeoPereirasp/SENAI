from uuid import uuid4, UUID

def gera_email(nome: str,
               sobrenome:str,
               dominio: str = "@senai.com") -> str:
    """
    uma função que gera email
    :param nome: nome do usuário
    :param sobrenome: sobrenome do usuário
    :param dominio: domínio da empresa
    :return: um email no formato nome.sobrenome@dominio.com
    """
    return f"{nome.lower()}.{sobrenome.lower()}{dominio}"

def gerador_id() -> UUID:
    """
    Função que gera um uuid
    :return:
    """
    return uuid4()


