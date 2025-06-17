# print("Hello World")
# print("Outra Coisa")

# Tipos de Dados - 4 Primitivos

# Int - Números Inteiros
# print(10)
# print(type(10))
# print(type(0))
# print(type(-10))

# Float- Números com Casas Decimais
# print(10.1)
# print(type(10.0))
# print(type(0.0))
# print(type(-10.0))

# String - Texto *
# print("Olá mundo!")
# print(type("Oi"))
# print(type("senha123"))
# print(type("123"))
# print(type("print(type(10))"))
# print("print(type(10))")

# Boolean - Tipo Lógico
# print(True)
# print(Fidadelse)
# print(type(True))

# Complex - Números Complexos
# print(type(1 + 2j))

# Variável
# idade = 25
# print(idade)
# print(type(idade))
# print(id(idade))

# Case Sensitive
# quantidade = 10
# Quantidade = 20
# print(id(quantidade))
# print(id(Quantidade))

# snake_case
# codigo_do_produto = "#QA12"

# # Regras - Números, Char Especiais, Palavras Reservadas
# # 1berto = True = não pode
# codigo_1 = "pode"
# # no%m*e$ = 10 = não pode

# if = "não pode"
# as = "não pode"

# import keyword
# print(*keyword.kwlist, sep="\n")

# Print
# codigo_produto = "#2"
# quantidade_produto = 100
# preco_produto = 3.50

# print(codigo_produto, quantidade_produto,
#       preco_produto, sep=' -> ', end=' final')
# print()
# print("Outra Coisa")

# Concatenação de Strings

# Produto: #2, Quantidade: 100, Preço: R$ 3.50

# nome = "Thiago"
# sobrenome = "Lima"

# nome_completo = nome + " " + sobrenome
# print(nome_completo)

# print("Produto: " + codigo_produto + ", Quantidade: " + str(quantidade_produto) + ", Preço: R$" + str(preco_produto))

# F-String

# nome = "Thiago"
# sobrenome = "Lima"
# nome_completo = f"{nome} {sobrenome}"
# print(nome_completo)

# Produto: #2, Quantidade: 100, Preço: R$ 3.50
# print(f"Produto: {codigo_produto} , Quantidade: {quantidade_produto}, Preço: R$ {preco_produto:.2f}")

# Input de Dados

# codigo_produto = input("Digite o código do produto: ")
# quantidade_produto = int(input("Digite a quantidade do produto: "))
# preco_produto = float(input("Digite o preço do produto: "))
#
# print(type(quantidade_produto))
#
# print(f"Produto: {codigo_produto} , Quantidade: {quantidade_produto}, Preço: R$ {preco_produto:.2f}")


# Formatadores

numero = 100_000_000_000
porcent = 0.7
print(f"{numero:,}")
print(f"{porcent:.2%}")
