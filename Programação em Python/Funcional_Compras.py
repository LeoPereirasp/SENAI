# Teste da Aplicação do Carrinho de Compras
from entities.compras import Cliente, Produtos, Carrinho, Endereco, Pedido

# Endereço
e1: Endereco = Endereco("Av. Brasil", "1000", "Rio de Janeiro", "RJ", "Brasil", "22000-000")
print("\n Endereço criado:")
print(e1)
print("-" * 100)

# Cliente
c1: Cliente = Cliente("Leo", e1)
print("Cliente criado:")
print(c1)
print("-" * 100)

# Teste de Produtos e subtotal
p1: Produtos = Produtos("Notebook", 1, 3500.00)
p2: Produtos = Produtos("Fone de Ouvido", 2, 150.00)
print("Produtos criados:")
print(p1)
print(p2)
print("-" * 100)

# Teste de Carrinho: add, remover, total
carrinho: Carrinho = Carrinho()
carrinho.add_produto(p1)
carrinho.add_produto(p2)
print("Carrinho após adicionar produtos:")
print(carrinho)
print("-" * 100)

# Remover produto
carrinho.remove_produto("Notebook")
print("Carrinho após remover 'Notebook':")
print(carrinho)
print("-" * 100)

# Add novamente para fechar o pedido
carrinho.add_produto(p1)

# Teste de Pedido e confirmação
pedido: Pedido = Pedido(c1, carrinho, "PIX")
print("Pedido criado (sem confirmação):")
print(pedido)
print("-" * 100)

print("Confirmando pedido...")
pedido.confirmar_pedido()
