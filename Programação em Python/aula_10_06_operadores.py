# Operadores Matemáticos
a = 10
b = 5

# Soma
print(a + b)
print(a + (-b))
print(-a + (-b))
print(a + b - 2.4)

# Subtração
print(a - b)
print(a - (-b))
print(-a - (-b))
print(a - b - 5.5)

# Multiplicação
print( 2 * 10)
print( 2 * (-10))
print(-2 * -10)

# Divisão Simples
print(10 / 3)
print(10 / 2)
print(10 / -2)
print(-10 / -2)

# Divisão Inteira
print(10 // 3)
print(10 // 2)
print(10 // -2)
print(-10 // -2)

# Módulo (MOD)
print(10 % 3) # Sinal de porcentagem significa resto
print(10 % 2) # Descobrir o resto de 10 dividido por 2 (EXEMPLO)
print(10 % -2)
print(-10 % -2)

area = 50
lata_grande = 18
lata_pequena = 3.5

quantidade_latas_grandes = area / lata_grande
quantidade_latas_pequenas = area % lata_grande // lata_pequena
print(f"""
Quantidade de Latas de 18L: {quantidade_latas_grandes}
Quantidade de Latas de 3.5L: {quantidade_latas_pequenas}
""")

from math import floor,ceil  # Bibliotecas de "arredondamento"
print(floor(10.3688669600987))
print(ceil(10.3688669600987))
print(round(10.3688669600987, 5))

# Exponenciação
print(10 ** 2)
print(10 ** 3)
print(5 ** 5)
print(5 ** -2)
print(pow(5,5))

# Exemplo - 1
# valor_metro_quadrado = float(input("Valor por m²: "))
# area_terreno = float(input("Área em m²: "))
# valor_terreno = valor_metro_quadrado * area_terreno
#
# print(f"O valor total do terreno é de: R$ {valor_terreno:,.2f}")

# Exemplo 2
# Cálculo das raízed de uma equação do segundo grau
# ax² + bx + c
from math import sqrt

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

delta = b ** 2 - (4 * a * c)

x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b + sqrt(delta)) / 2 * a

print(f"As raízes da equação {a}x² + {b}x + {c}")
print(f"S = {x1},{x2}")

