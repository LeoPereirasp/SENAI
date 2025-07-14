from uuid import uuid4, UUID
from typing import List

class Endereco:

    logradouro: str
    numero: str
    cidade: str
    estado: str
    cep: str

    def __init__(self, logradouro: str,
                 numero: str, cidade: str, estado: str, cep: str):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __repr__(self):
        return (f"{self.logradouro}, {self.numero} - {self.cidade} - "
                f"{self.estado}, {self.cep}")

class Livro:
    nome: str
    autor: str
    ano: int

    def __init__(self, nome: str, autor: str, ano: int):
        self.nome = nome
        self.autor = autor
        self.ano = ano

    def __repr__(self):
        return f"{self.nome} - {self.autor}, {self.ano}"

class Membro:
    nome: str
    n_cadastro: UUID
    endereco: Endereco
    livros: List[Livro]

    def __init__(self, nome: str, endereco: Endereco):
        self.nome = nome
        self.n_cadastro = uuid4()
        self.endereco = endereco
        self.livros = []

    def __repr__(self):
        return f"Nome: {self.nome}, Nº Cadastro: {self.n_cadastro}"

class Biblioteca:
    nome: str
    acervo: List[Livro]
    membros: List[Membro]

    def __init__(self, nome):
        self.nome = nome
        self.acervo = []
        self.membros = []

    def cadastrar_membro(self, membro: Membro) -> None:
        self.membros.append(membro)

    def emprestimo(self, livro: Livro, membro: Membro):
        if membro in self.membros:
            self.acervo.remove(livro)
            membro.livros.append(livro)
        else: print(f"{membro.nome} não é membro.")

    def devolucao(self, livro: Livro, membro: Membro):
        self.acervo.append(livro)
        membro.livros.remove(livro)

    def receber(self, livro: Livro):
        self.acervo.append(livro)

    def __repr__(self):
        return f"Biblioteca: {self.nome}"