# Programação Orientada a Objetos

# Classes
# Objetos - instância
# Atributos
# Métodos

# Herança
# Polimorfismo
# Encapsulamento

# PascalCase
class ClienteLoja:
    # Listar os atributos
    nome: str
    cpf: str
    endereco: str

    def compra(self, produto: str, quantidade: int, preco: float) -> None:
        print(f"""
        ---Dados da Compra---
        Nome: {self.nome}
        Produto: {produto.title()}
        Quantidade: {quantidade} und
        Preço Unitário: R$ {preco:,.2f}

        Total da Compra: R$ {quantidade * preco:,.2f}
        """)

    # Construtor
    def __init__(self, nome, cpf, endereco):
        self.nome =nome
        self.cpf = cpf
        self.endereco = endereco

    # Representação
    def __repr__(self):
        return f"Nome: {self.nome}, End: {self.endereco}"

joao_silva: ClienteLoja = ClienteLoja("João", "1", "Rua do Senai")
print(joao_silva.nome)
print(joao_silva.cpf)
print(joao_silva.endereco)

ana_macedo = ClienteLoja = ClienteLoja("Ana", "2", "Rua da Escola")
print(ana_macedo.nome)
print(ana_macedo.cpf)
print(ana_macedo.endereco)

joao_silva.compra("caderno", 2, 25)
ana_macedo.compra("caneta", 5, 7.5)

class Carro:
    marca: str
    modelo: str
    ano: int
    cor: str

    def __init__(self,     marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def pintar(self, cor: str) -> None:
        self.cor = cor

    def corrida_app(self, distancia: float, valor_km: float) -> float:
        return distancia * valor_km

    def __repr__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo},"
                f"Ano: {self.ano}, Cor: {self.cor}")

onix : Carro = Carro("Chevrolet", "Onix", 2019, "prata")

# print(onix.marca)
# print(onix.modelo)
# print(onix.ano)
# print(onix.cor)
print(onix)
onix.pintar("vermelho")
print(onix)

valor_corrida = onix.corrida_app(10, 6)
print(valor_corrida)


# Importando
from entities.banco import ClienteBanco,ClienteBancoPrata,ClienteBancoOuro

cb1: ClienteBanco = ClienteBanco("João", 1000)

print(cb1)
print(cb1.id)

cp1: ClienteBancoPrata = ClienteBancoPrata("Ana", 10000)

print(cp1)
print(cp1.categoria)
print(cp1.pontos)
cp1.deposito(5000)
print(cp1)
print(cp1.pontos)

co1: ClienteBancoOuro = ClienteBancoOuro("Thiago", 100000)
co1.superdeposito(5000)
print(co1)


