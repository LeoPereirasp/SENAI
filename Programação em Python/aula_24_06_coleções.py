# Coleções
a : int = 10
texto : str = "oi"

# Listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_mista = [10, 3.14, "oi", True]

print(type([]))

for elemento in lista:
    print("oi" * elemento)

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Índice
numeros = list(range(50))
print(numeros)
print(numeros[0])
print(numeros[4])
print(numeros[-4])

print(list("Tipo assim olha"))

# Slicing
print(numeros[10:30])
print(numeros[:24])
print(numeros[7:])
print(numeros[-1:-30:-1])
print(numeros[10:40:2])
print(numeros[::-1])

