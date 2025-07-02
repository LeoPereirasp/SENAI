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
#
# # Com List Comprehension
# alunos_7_mais =[aluno for aluno in alunos if aluno["média"] >= 7]
# print(alunos_7_mais)

# List Comprehension
# Uma forma de criar listas , de forma declarativa

lista = list(range(50))
lista_quadrado = []

for n in lista:
    lista_quadrado.append(n ** 2)
print(lista_quadrado)
lista_quadrado = [n ** 2 for n in lista]
print(lista_quadrado)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []
for n in lista:
    if n % 2 == 0:
        lista_pares.append(n)
print(lista_pares)
lista_pares = [n for n in lista if n % 2 == 0]
print(lista_pares)

impares_pares = [
    "par" if n % 2 == 0 else "ímpar" for n in lista
]

alunos = {
    "João": ".", "Ana": "|", "Daniel": "|", "Maria": "."
}

presenca = [aluno
            for aluno in alunos
            if alunos[aluno] == "."]
print(presenca)