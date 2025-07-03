
from funcoes.banco import criar_conta, depositar, sacar, consultar_saldo

def main():
    while True:
        print("\n--- Banco Funcional ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Consultar Saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do titular: ")
            numero = input("Número da conta: ")
            saldo = float(input("Saldo inicial: "))
            print(criar_conta(nome, numero, saldo))

        elif opcao == "2":
            numero = input("Número da conta: ")
            valor = float(input("Valor para depósito: "))
            print(depositar(numero = numero, valor = valor))

        elif opcao == "3":
            numero = input("Número da conta: ")
            valor = float(input("Valor para saque: "))
            print(sacar(numero = numero, valor = valor))

        elif opcao == "4":
            numero = input("Número da conta: ")
            print(consultar_saldo(numero = numero))

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()