# Sets (Conjuntos)
# Seguem a teoria matemáticas dos conjuntos
# Não aceitam valores repetidos
# Sem ordem fixa
# Não temos índice e slicing

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s)
print(type(s))

# Funções Ùteis
print(len(s))
print(sum(s))
print(max(s))
print(min(s))

s_misto = {"oi", 10, True}
print(s_misto)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Métodos de sets
# Adicionando valores
s2.add(7)
print(s2)

# Remover valores
s2.remove(3)
print(s2)

# Métodos de Conjuntos
# União
s_uniao = s1.union(s2)
print(s_uniao)

# Intersecção
s_interseccao = s1.intersection(s2)
print(s_interseccao)

# Diferença
s_diferenca = s1.difference(s2)
print(s_diferenca)

# Exemplo - Pesquisa de Mercado
japa = []
mex = []

for i in range(5):
    nome = input("Nome: ")
    if nome:
        voto = input("J(apa) ou M(ex) ou A(mbos)?").upper()
        if voto == "J": japa.append(nome)
        elif voto == "M": mex.append(nome)
        elif voto == "A":
            japa.append(nome)
            mex.append(nome)
        else: print("Opção Inválida")

japa = set(japa)
mex = set(mex)

japa = {'ana', 'math', 'leo', 'rafa', 'thiago'}
print(f"Japa teve {len(japa)} votos.")

mex = {'math', 'leo', 'rafa', 'thiago'}
print(f"Mex teve {len(mex)} votos.")

print(f"Ambos tiveram {len(japa.intersection(mex))}")

