# Expressões Lambda -> Funções Lambda
dobro = lambda x: x * 2
print(dobro(2))

email = lambda nome: f"{nome.split()[0]}.{nome.split()[1]}@senai.com"
print(email("thiago lima"))

exp = lambda b, e: b ** e
print(exp(2, 8))

# Exemplo de Ordenação
from statistics import mean
alunos = [
    {"nome": "João", "idade": 20, "notas": [5, 6, 5, 7]},
    {"nome": "Ana", "idade": 20, "notas": [9, 8, 5, 7]},
    {"nome": "Daniel", "idade": 19, "notas": [5, 6, 3, 3]},
    {"nome": "Maria", "idade": 10, "notas": [9, 9, 9, 9]},
]

for aluno in alunos:
    aluno["média"] = mean(aluno["notas"])

alunos.sort(key= lambda aluno: aluno["média"])
print(*alunos, sep="\n")

# Map & Filter
# def dobro(n: int | float = 0) -> int | float:
#     return n * 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_dobro = list(map(lambda x: x * 2, lista))
print(lista_dobro)

# for n in lista:
#     lista_dobro.append(dobro(n))
# print(lista_dobro)

# Exemplo com Média
from statistics import mean

alunos = {
    "John": [7, 4, 5],
    "Maria": [5, 8, 9],
    "Peter": [6, 7, 7],
    "Alice": [7, 4, 10]
}

medias_alunos = list(map(lambda notas: round(mean(notas), 2), alunos.values()))
print(medias_alunos)

# Filter
# def par(n: int | float = 0) -> bool:
#     return n % 2 == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_par = list(filter(lambda n: n % 2 == 0, lista))
print(lista_par)

# for n in lista:
#     if par(n=n):
#         lista_par.append(n)
#     else: pass

# Exemplo com Aliunos Aprovados(Média >= 7)
from statistics import mean

alunos = {
    "John": [7, 4, 5],
    "Maria": [5, 8, 9],
    "Peter": [6, 7, 7],
    "Alice": [7, 4, 10]
}

alunos_aprovados = dict(filter(lambda notas: round(mean(notas[1]) >= 7, 2), alunos.items()))
print(alunos_aprovados)