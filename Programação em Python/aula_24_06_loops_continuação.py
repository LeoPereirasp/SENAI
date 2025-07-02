# Loop While

# n1 = input("N1: ")
# n2 = input("N2: ")
#
# n1_is_number = n1.isdigit()
# n2_is_number = n2.isdigit()
#
# while not n1_is_number or not n2_is_number:
#     print("N1 e N2 devem ser numéricos!")
#     n1 = input("N1: ")
#     n2 = input("N2: ")
# else:
#     print(f"Sua média é de: {(float(n1)) + (float(n2)) / 2:.2f} ")

# continue e break
tentativas = 0
while True:
    if tentativas < 3:
        email = input("email: ")
        if email == "thiago":
            senha = input("Senha: ")
            if senha == "123":
                print("Bem-Vindo(a)!")
                break
            else:
                print("Senha incorreta")
                tentativas += 1
                continue
        else:
            print("Usuário incorreto!")
            continue
    else:
        print("Número de Tentativas esgotado!")
        break