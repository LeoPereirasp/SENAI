# Exercício 1 - Tabuada
tabuada = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {tabuada}:")
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")

# #  Código do Professor
# for i in range(1,11):
#     print(f"{tabuada} X {i} = {tabuada * i}")
#
# i = 1
# while i < 11:
#     print(f"{tabuada} X {i} = {tabuada * i}")
#     i += 1

# Exercício 2 - Lista de Despesas
contador = 1
total = 0
quantidade_despesas = int(input("Quantas compras foram realizadas: "))

while contador <= quantidade_despesas:
    valor_compra = float(input(f"Digite o valor da compra {contador}: "))
    total += valor_compra
    contador += 1

print(f"Você gastou um total de R$ {total:.2f}")

# # Código do Professor
# quantidade_despesas = int(input("Quantas compras foram realizadas: "))
# total = 0
#
# for i in range(1, quantidade_despesas + 1):
#     despesa = float(f"Valor da despesa {i}: R$ ")
#     total += despesa
#
# print(f"Seu total de gastos é de: R$ {total:,.2f}")

# Exercício 3 - Sistema de banco simples
saldo = 0
while True:
    print("Menu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("s - Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == '1':
        valor = float(input("Digite o valor para depósito: R$ "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    elif opcao == '2':
        valor = float(input("Digite o valor para saque: R$ "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    elif opcao == 's':
        break
    else:
        print("Opção inválida. Tente novamente.")

print(f"\nOperação encerrada. Saldo final: R$ {saldo:.2f}")

# # Código do Professor
# import time
# saldo = 0
# while True:
#     operacao = input(
#     """
#     [ 1 ] => Depósito
#     [ 2 ] => Saque
#     [ 3 ] => Consultar Saldo
#     [ s ] => Sair
#     """
#     ).lower()
#
#     if operacao == "s":
#         for i in range(1,4):
#             print("\r", end="Saindo " + "." * i)
#             time.sleep(1)
#         break
#     elif operacao == "1":
#         print()
#         print("--- Depósito ---")
#         valor = float(input("Valor: R$ "))
#         saldo += valor
#     elif operacao == "2":
#         print()
#         print("--- Saque ---")
#         valor = float(input("Valor: R$ "))
#         if valor <= saldo: saldo -= valor
#         else: print("Saldo Insuficiente!")
#     elif operacao == "3":
#         print(f"Seu saldo atual é de: R$ {saldo:,.2f}")
#         continue
#     else:
#         print("Opção Inválida!")
#         continue
# print()
# print(f"Seu saldo atual é de: R$ {saldo:,.2f}")


