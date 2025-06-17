# Loops
# import string
# palavra = "oi"
#
# for letra in palavra:
#     print(letra)
#
# senha = "senha123"
# tem_numero = False
# tem_letra = False
# print(string.digits)
# print(string.ascii_letters)
#
# for char in senha:
#     if char in string.digits:
#         tem_numero = True
#     elif char in string.ascii_letters:
#         tem_letra = True
# if tem_numero and tem_letra:
#     print("Senha Cadastrada.")
#
# # For com Range
# r = range(1, 50, 2)
# print(*r)
# print(len(r))
#
# for i in range(1, 50, 5):
#     print(i ** 2)
#
# n = int(input("N:"))
#
# for i in range(n):
#     print(f"{i} é par." if i % 2 == 0 else f"{i} é ímpar.")
#
# quantidade_alunos = 3
#
# for i in range(quantidade_alunos):
#     nome = str(input("Digite seu Nome: "))
#     n1 = float(input("Digite a Nota 1:"))
#     n2 = float(input("Digite a Nota 2:"))
#     media = (n1 + n2) / 2
#     print(f"{nome}, sua situação é: ", end="")
#     if n1 > 10 or n2 > 10:
#         print("Nota Inválida! Por favor informe uma nota de 0 a 10 em ambos os campos!")
#     elif media == 10:
#         print("Aprovado com Distinção")
#     elif media >= 7:
#         print("Aprovado")
#     elif media < 7:
#         print("Reprovado")

# Loop While
# Repetição Condicional

i = 0

while i < 10:
    print(i)
    # i = i + 1
    i += 1

usuario = input("user: ")

while usuario != "thiago":
    print("Usuário incorreto!")
    usuario = input("user: ")

senha = input("senha: ")