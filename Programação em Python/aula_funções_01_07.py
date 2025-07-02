# Funções
# Um mini software, um mini código
# Modularização
# Reutilização de código
# Abstração
# Mais legível

# def nome_da_funcao():
#     pass

# Criar
# def primeira_funcao():
#     print("minha primeira função.")
#
# # Executar - Function call
# primeira_funcao()
# print(primeira_funcao)
#
# # Escopo Global X Escopo Local
# a = 42
# b = 0
# def func():
#     global a, b
#     a = 10
#     b = 20
#     print(a + b)
# func()
# print(a)
# print(b)
#
# # Função Que Realizam
# def saudacao():
#     nome = input("Nome: ")
#     print("Boa Noite,", nome)
# saudacao()
# # texto = saudacao()
# # print(texto)
#
# # Função Que Retornam
# def gera_saudacao():
#     nome = input("Nome: ")
#     return f"Boa Noite, {nome}"
#     # print("oi") - não aparece após o return
# gera_saudacao()
#
# print(gera_saudacao())
# texto = gera_saudacao()
#
# print(texto.upper())
#
# def soma():
#     a = int(input("A: "))
#     b = int(input("B: "))
#     return a + b
# res = soma()
# print(res)
#
# def area_circunferencia():
#     from math import pi

#     raio = float(input("raio: "))
#     return round(pi * raio ** 2, 2)

# area = area_circunferencia()
# print(area)

# Parâmetros
def area_circunferencia(raio):
    from math import pi
    return f"{pi * raio ** 2:.2f}"

area = area_circunferencia(1)
print(area)

def soma(a: int = 0, b: int = 0) -> int:
    return a + b

res = soma(10, 5)
res_2= soma(10)
res_3= soma(b = 5)
print(res)
print(res_2)
print(res_3)

print(soma(5, 5))
print(soma("5", "5"))

def gera_email(nome: str, sobrenome:str, dominio: str = "@senai.com") -> str:
    return f"{nome.lower()}.{sobrenome.lower()}{dominio}"

print(gera_email("Thiago", "Lima"))

nomes = ["João Silva", "Ana Santos", "Daniel Oliveira", "Maria Rita"]
dominio = "@gmail.com"

for pessoa in nomes:
    nome = pessoa.split()[0]
    sobrenome = pessoa.split()[1]
    print(gera_email(nome = nome, sobrenome = sobrenome, dominio = dominio))