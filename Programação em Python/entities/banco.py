from uuid import uuid4, UUID
from funcoes.utilitarios_banco import gera_conta

class ClienteBanco:
    id: UUID
    nome: str
    conta: str
    saldo: float

    def __init__(self, nome, saldo):
        self.id = uuid4()
        self.nome = nome
        self.conta = gera_conta()
        self.saldo = saldo

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= self.saldo: self.saldo -= valor
        else: print("Saldo insuficiente!")

    def __repr__(self):
        return (f"Nome: {self.nome}, Conta: {self.conta},"
                f"Saldo: R$ {self.saldo:,.2f}")

# Herança
class ClienteBancoPrata(ClienteBanco):
    categoria: str = "Prata"
    pontos: int

    def __init__(self, nome, saldo):
        super().__init__(nome,saldo)
        self.pontos = saldo // 5

    # Polimorfismo
    def deposito(self, valor: float) -> None:
        super().depositar(valor)
        self.pontos += valor // 5


class ClienteBancoOuro(ClienteBancoPrata):
    def superdeposito(self, valor: float) -> None:
        super().deposito(valor)
        self.saldo += valor * 0.05
