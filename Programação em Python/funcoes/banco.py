
banco = {}

def criar_conta(nome: str, numero: int, saldo_inicial: float) -> str | int | float:
    """
    Cria uma nova conta no banco.

    :param nome: Nome do titular.
    :param numero: Número da conta (deve ser único).
    :param saldo_inicial: Saldo inicial da conta.
    :return: Mensagem de sucesso ou erro.
    """
    if numero in banco:
        return "Conta já existe."
    banco[numero] = {"nome": nome, "saldo": saldo_inicial}
    return "Conta criada com sucesso."


def depositar(numero: str, valor: float) -> str | float:
    """
    Deposita um valor em uma conta existente.

    :param numero: Número da conta.
    :param valor: Valor a ser depositado.
    :return: Mensagem de sucesso ou erro.
    """
    if numero not in banco:
        return "Conta não encontrada."
    if valor <= 0:
        return "Valor inválido."
    banco[numero]["saldo"] += valor
    return "Depósito realizado com sucesso."


def sacar(numero: str, valor: float) -> str | float:
    """
    Realiza um saque na conta.

    :param numero: Número da conta.
    :param valor: Valor a ser sacado.
    :return: Mensagem de sucesso ou erro.
    """
    if numero not in banco:
        return "Conta não encontrada."
    if valor <= 0:
        return "Valor inválido."
    if banco[numero]["saldo"] < valor:
        return "Saldo insuficiente."
    banco[numero]["saldo"] -= valor
    return "Saque realizado com sucesso."


def consultar_saldo(numero: str) -> str:
    """
    Retorna o saldo da conta.

    :param numero: Número da conta.
    :return: Saldo ou mensagem de erro.
    """
    if numero not in banco:
        return "Conta não encontrada."
    saldo = banco[numero]["saldo"]
    nome = banco[numero]["nome"]
    return f"Titular da Conta: {nome} | Saldo: R$ {saldo:.2f}"