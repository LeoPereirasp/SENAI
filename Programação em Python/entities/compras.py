from uuid import uuid4, UUID

class Endereco:
    rua: str
    numero: str
    cidade: str
    estado: str
    pais: str
    cep: str

    def __init__(self, rua: str, numero: str, cidade: str, estado: str, pais: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.cep = cep

    def __repr__(self) -> str:
        return f"{self.rua}, {self.numero} - {self.cidade} - {self.estado}, {self.pais} - CEP: {self.cep}"

class Cliente:
    nome: str
    n_cadastro: UUID
    endereco: Endereco

    def __init__(self, nome: str, endereco: Endereco):
        self.nome = nome
        self.n_cadastro = uuid4()
        self.endereco = endereco

    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Nº Cadastro: {self.n_cadastro}\nEndereço: {self.endereco}"


class Produtos:
    nome: str
    quantidade: int
    valor: float

    def __init__(self, nome: str, quantidade: int, valor: float):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def subtotal(self) -> float:
        return self.quantidade * self.valor

    def __repr__(self) -> str:
        return f"{self.nome} (x{self.quantidade}) - R$ {self.valor:.2f} cada | Subtotal: R$ {self.subtotal():.2f}"


class Carrinho:
    produtos: list

    def __init__(self):
        self.produtos = []

    def add_produto(self, produto: Produtos):
        self.produtos.append(produto)

    def remove_produto(self, nome: str):
        self.produtos = [p for p in self.produtos if p.nome != nome]

    def total(self) -> float:
        return sum(p.subtotal() for p in self.produtos)

    def __repr__(self) -> str:
        if not self.produtos:
            return "Carrinho vazio."
        texto = "\n".join([str(p) for p in self.produtos])
        return f"{texto}\nTotal: R$ {self.total():.2f}"


class Pedido:
    cliente: Cliente
    carrinho: Carrinho
    pagamento: str

    def __init__(self, cliente: Cliente, carrinho: Carrinho, pagamento: str):
        self.cliente = cliente
        self.carrinho = carrinho
        self.pagamento = pagamento

    def confirmar_pedido(self):
        print("\n📦 PEDIDO CONFIRMADO COM SUCESSO!")
        print("-" * 50)
        print(f"Cliente: {self.cliente.nome}")
        print(f"N° de Cadastro: {self.cliente.n_cadastro}")
        print(f"Endereço de entrega: {self.cliente.endereco}")
        print("-" * 50)
        print("Itens do Carrinho:")
        for produto in self.carrinho.produtos:
            print(
                f"- {produto.nome} (x{produto.quantidade}) - R$ {produto.valor:.2f} | Subtotal: R$ {produto.subtotal():.2f}")
        print("-" * 50)
        print(f"TOTAL DO PEDIDO: R$ {self.carrinho.total():.2f}")
        print(f"Pagamento via: {self.pagamento}")
        print("-" * 50)
        print("Obrigado pela sua compra!\n")

    def __repr__(self) -> str:
        return (f"----- DADOS DO PEDIDO -----\n"
                f"{self.cliente}\n\n"
                f"Carrinho:\n{self.carrinho}\n"
                f"Forma de Pagamento: {self.pagamento}")