# # Listas
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numeros + [10, 11, 12])
# print(numeros * 2)
# print(numeros[1])
# print(numeros[1:7])
# print(numeros[::2])
#
# # Funções Úteis
# print(len(numeros))
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))
#
# # Métodos de Listas
# # OBS: Alguns métodos são executados no que chamamos in-place
#
# # Adicionar itens
# frutas = ["laranja", "uva", "abacaxi"]
#
# frutas.append("maçã")
# print(frutas)
# print(len(frutas))
# print(*frutas, sep="\n")
#
# frutas.extend(["morango", "manga"])
# print(frutas)
# print(len(frutas))
# print(*frutas, sep="\n")
#
# frutas.insert(2,"melão")
# print(frutas)
#
# # Editar um item da lista
# # frutas[4] = "limão"
# frutas[frutas.index("maçã")] = "limão"
# print(frutas)
#
# # Remove itens da lista
# frutas.remove("limão")
# print(frutas)
#
# # ultima_fruta = frutas.pop(0)
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
#
# del frutas [4]
# print(frutas)
#
# # Ordenar itens
# frutas.sort()
# print(frutas)
# frutas.sort(reverse=True)
# print(frutas)
#
# frutas_ordenadas = sorted(frutas)
# print(frutas_ordenadas)
#
# print(sorted("hjbhkjvkigu"))
#
# # Tuplas
# # Tuplas se parecem com listas
# # Tuplas são imutáveis
# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# # Índice e Slicing
# print(tupla[5])
# print(tupla[::2])
#
# for i in tupla:
#     print(i ** 2)
#
# print(tupla.count(1))
#
# tupla_mista = ("oi", 10, 3.15, [], ())
# tupla_mista[3].append(1)
# print(tupla_mista)
#
# # Funções Úteis
# print(len(tupla))
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
#
# # Tuple Unpacking
# tupla1 = (1, 2, 3)
# a, b, c = (1, 2, 3)
# print(a)
# print(b)
# print(c)
#
# # Dicionários
# # Dicionários são como listas evoluídas
# # Dicionários são mutáveis
#
# dicionario = {"a":1, "b":2, "c":3}
#
# dados = {
#     "nome": "Thiago",
#     "idade": 26,
# }
# print(dados)
# print(dados["nome"])
# print(dados["idade"])
#
# print(len(dados))
#
# # Utilizando chaves
# # Consulta
# print(dados["nome"])
#
# # Adicionar
# dados["email"] = "thiago@email.com"
# print(dados)
#
# dado = input("Dado novo: ")
# valor = input("Valor: ")
# dados[dado] = valor
#
# dados.update({
#     "sobrenome": "Lima",
#     "nacionalidade": "BR"
# })
#
# # Editar
# dados["idade"] = 27
# print(dados)
#
# # Deletar
# del dados["altura"]
# print(dados)

# Métodos
# produtos = {
#     "cebola": 100,
#     "macarrão": 150,
#     "açúcar": 170,
#     "leite": 200
# }
#
# # Apenas as Chaves
# print(produtos.keys())
#
# for k in produtos.keys():
#     print(k.upper())
#
# # Apenas os Valores
# print(list(produtos.values()))
# print(sum(list(produtos.values())))
#
# for v in produtos.values():
#     print(v)
#
# # Chaves e Valores
# print(produtos.items())
#
# for chave, valor in produtos.items():
#     print(chave, valor)
#
# nomes = ["joão", "ana", "maria", "daniel"]
# telefones = [1, 2, 3, 4]
#
# contatos = dict(zip(nomes, telefones))
# print(contatos)

# Exemplo com Estoque
estoque = {}

while True:
    produto = input("Produto (ou  enter para sair): ")

    if produto:
        quantidade = int(input(f"Quantidade de {produto}: "))
        estoque[produto] = quantidade
    else:
        print("Saindo...")
        break

print()
print("--- Resumo do Estoque ---")

if estoque:
    for k, v in estoque.items():
        print(f"{k}: {v} unidades")
    print()
    print(f"Temos um total de {sum(estoque.values())} itens em estoque")
else:
    print("O estoque está vazio 😒")

# Shalllow
a = [1, 2, 3, 4]
b = a
print(a)
print(b)
b.append(5)
print(a)
print(b)
print(id(a))
print(id(b))

# Deep
a = [1, 2, 3, 4]
b = a.copy()
print(a)
print(b)
b.append(5)
print(a)
print(b)
print(id(a))
print(id(b))


