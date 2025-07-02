from funcoes.funcoes import gera_email, gerador_id

def main():
    while True:
        dominio = input("Para qual empresa serão gerados os emails: ")
        nome = input("Nome (ou enter): ")
        if nome:
            sobrenome = input("Sobrenome: ")
            print(gera_email(nome = nome,
                             sobrenome = sobrenome,
                             dominio = dominio))
            print(f"Id {nome}: {gerador_id()}")
        else:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()