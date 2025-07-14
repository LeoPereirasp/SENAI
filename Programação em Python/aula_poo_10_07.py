from entities.biblioteca import Membro, Endereco, Livro, Biblioteca

# Encapsulamento

e1: Endereco = Endereco("Rua A", "10", "SBC",
                        "SP", "00000-000")
m1: Membro = Membro("João", e1)

o_pianista: Livro = Livro("O Pianista", "W. Szpilman", 1946)
ivan_ilitch: Livro = Livro("A Morte de Ivan Ilitch", "Tolstói", 1950)
jantar_secreto: Livro = Livro("Jantar Secreto", "Raphael Montes", 2016)


print(o_pianista)
print(ivan_ilitch)
print(jantar_secreto)

biblioteca_senai: Biblioteca = Biblioteca("Senai")

biblioteca_senai.receber(o_pianista)
biblioteca_senai.receber(ivan_ilitch)
biblioteca_senai.receber(jantar_secreto)

print(biblioteca_senai.acervo)

biblioteca_senai.cadastrar_membro(m1)
print(biblioteca_senai.membros)

biblioteca_senai.emprestimo(o_pianista, m1)
print(biblioteca_senai.acervo)
print(m1.livros)

m2: Membro = Membro("Ana", e1)

biblioteca_senai.emprestimo(ivan_ilitch, m2)