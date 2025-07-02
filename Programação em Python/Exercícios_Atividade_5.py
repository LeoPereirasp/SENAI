# Exercício 1
frutas = ["maçã", "banana", "laranja", "melancia", "uva"]
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])
frutas.extend(["abacaxi", "kiwi", "banana"])
print(frutas)
del frutas[1]
frutas.sort()
print("Quantidade de 'banana':", frutas.count("banana"))
print("Lista final:", frutas)

# Código do Professor
# from collections import Counter

# frutas = ["banana", "uva", "morango", "laranja"]
# print(frutas[0])
# print(frutas[-1])

# frutas.extend(["limão", "abacate", "maçã"])
# print(frutas)

# del frutas[1]
# frutas.sort()
# print(frutas)

# print(frutas.count("banana"))
# print(Counter(frutas))

# Exercício 2
dados = ("Leo",18, "SBC")
print(dados[0])
print(dados[1])
print(dados[2])
# dados[0] = "Thiago"
# TUPLAS SÃO IMUTAVEIS em tempo de execução, então por isso esse comando não funciona.
tupla_hobies = ('futebol', 'video-game')
tupla_concat = dados + tupla_hobies
print(tupla_concat)


# # Código do Professor
# dados = "Thiago", 26, "São Paulo"
# for dado in dados:
#     print(dado)
# # OU
# print(*dados, sep="\n")

# # dados[0] = "Pedro"
# # Não posso alterar a tupla em tempo de execução, pois são como constantes para a aplicação.

# informacoes = dados + ("Leitura", "Surf", "Musculação")
# print(informacoes)


# Exercício 3
contatos = {
    "Ana": ["1234-5678"],
    "Carlos": ["8765-4321"],
    "Leo": ["99999-9999"]
}

contatos["Beatriz"] = ["1111-2222"]
del contatos["Carlos"]
contatos["Ana"] = ["9999-8888"]
print("Nomes dos Contatos:")
for nome in contatos:
    print(nome)

# Código do Professor
# contatos = {"João: 1", "Maria: 2", "Ana: [3, 4]", "Daniel: 5"}
# contatos["Alice"] = 6
# print(contatos)

# del contatos["Daniel"]
# print(contatos)

# contatos["Ana"][1] = 7
# print(contatos)

# print(*contatos.keys(), sep="\n")
# for nome in contatos.keys(): print(nome)

# # Exercício 4
produtos = {}
while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar novo produto")
    print("2 - Consultar produto")
    print("3 - Remover produto")
    print("4 - Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        produtos[nome] = {'preço': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' cadastrado com sucesso!")
    elif opcao == '2':
        nome = input("Digite o nome do produto a ser consultado: ")
        if nome in produtos:
            produto = produtos[nome]
            print(f"\nInformações do produto '{nome}':")
            print(f"Preço: R$ {produto['preço']:.2f}")
            print(f"Quantidade em estoque: {produto['quantidade']}")
        else:
            print(f"Produto '{nome}' não encontrado no cadastro.")
    elif opcao == '3':
        nome = input("Digite o nome do produto a ser removido: ")
        if nome in produtos:
            del produtos[nome]
            print(f"Produto '{nome}' removido com sucesso!")
        else:
            print(f"Produto '{nome}' não encontrado no cadastro.")
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

# # Código do Professor
# produtos = {"cebola":{
#                 "preço": 5,
#                 "quantidade": 100
#                 }}
# while True:
#     print("""
#     [A] -> ADICIONAR
#     [C] -> CONSULTAR
#     [E] -> EDITAR
#     [R] -> REMOVER
#     [S] -> SAIR
#     """)
#     opcao = input().lower()

#     if opcao == "s":
#         print("Saindo...")
#         break
#     elif opcao == "a":
#         print()
#         print("--- Adicionar Produto ---")
#         produto = input("Produto: ")
#         if produto in produtos.keys():
#             print("Produto já está cadastrado!")
#         else:
#             produtos.update({
#                 produto:{
#                     "preço": float(input(f"Preço {produto}: ")),
#                     "quantidade": int(input(f"Quantidade {produto}: "))
#                 }
#             })
#     elif opcao == "c":
#         print()
#         print("--- Consultar Produto ---")
#         produto = input("Produto: ")
#         if produto in produtos.keys():
#             print(f"Nome: {produto}")
#             print(f"Preço: R$ {produtos[produto]["preço"]}")
#             print(f"Quantidade: {produtos[produto]["quantidade"]}")
#         else:
#             print("Produto não cadastrado!")
#     elif opcao == "r":
#         print()
#         print("--- Remover Produto ---")
#         produto = input("Produto: ")
#         if produto in produtos.keys():
#             print(f"Tem certeza que deseja excluir {produto}?")
#             confirma = input("S ou N: ").lower()
#             if confirma == "s": del produtos[produto]
#             else: continue
#         else:
#             print("Produto não cadastrado!")

# print(*produtos.items(), sep="\n")


# Exercício 5
alunos = [
    {"nome": "Leo", "idade": 18, "notas": [8.0, 9.0, 9.0]},
    {"nome": "Thiago", "idade": 26, "notas": [6.0, 5.5, 6.5]},
    {"nome": "Carlos", "idade": 18, "notas": [7.0, 8.0, 7.0]},
    {"nome": "Gabriel", "idade": 17, "notas": [9.0, 9.0, 10.0]}
]
for aluno in alunos:
    notas = aluno["notas"]
    media = sum(notas) / len(notas)
    aluno["media"] = media
maior_media = 0
aluno_10 = None

for aluno in alunos:
    if aluno["media"] > maior_media:
        maior_media = aluno["media"]
        aluno_10 = aluno["nome"]
print(f"Aluno com a maior média: {aluno_10} ({maior_media:.2f})")

aprovados = []
for aluno in alunos:
    if aluno["media"] > 7:
        aprovados.append(aluno["nome"])
print("Alunos com média acima de 7:", aprovados)


# # Código do Professor
# from statistics import mean
# alunos = [
#     {"nome": "João", "idade": 20, "notas": [5, 6, 5, 7]},
#     {"nome": "Ana", "idade": 20, "notas": [9, 8, 5, 7]},
#     {"nome": "Daniel", "idade": 19, "notas": [5, 6, 3, 3]},
#     {"nome": "Maria", "idade": 10, "notas": [9, 9, 9, 9]},
# ]
#
# # Calcular média dos alunos
# for aluno in alunos:
#     aluno["média"] = mean(aluno["notas"])
# print(alunos)
#
# # Encontrar o aluno com maior média
# aluno_maior_media = {"nome": "", "média": 0}
#
# for aluno in alunos:
#     if aluno["média"] > aluno_maior_media["média"]:
#         aluno_maior_media["nome"] = aluno["nome"]
#         aluno_maior_media["média"] = aluno["média"]
# print(aluno_maior_media)
#
# # Listando alunos com média >= 7
# alunos_7_mais = []
#
# for aluno in alunos:
#     if aluno["media"] >= 7:
#         alunos_7_mais.append(aluno)
# print(*alunos_7_mais, sep="\n")