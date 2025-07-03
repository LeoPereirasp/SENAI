from funcoes.escola import (cadastrar_aluno,
                            registrar_nota, calcular_media, listar_alunos, boletim_aluno)

def main():
    while True:
        print("\n--- Sistema Escolar Bimestral ---")
        print("1. Cadastrar aluno")
        print("2. Registrar nota")
        print("3. Calcular média do aluno")
        print("4. Listar alunos")
        print("5. Imprimir boletim do aluno")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            print(cadastrar_aluno(nome = nome, matricula = matricula))

        elif opcao == "2":
            matricula = input("Matrícula do aluno: ")
            nota = float(input("Nota (0 a 10): "))
            print(registrar_nota(matricula = matricula, nota = nota))

        elif opcao == "3":
            matricula = input("Matrícula do aluno: ")
            print(calcular_media(matricula = matricula))

        elif opcao == "4":
            print(listar_alunos())

        elif opcao == "5":
            matricula = input("Matrícula do aluno: ")
            print(boletim_aluno(matricula = matricula))

        elif opcao == "6":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()