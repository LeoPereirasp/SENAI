#
# temperatura_f = float(input("Informe a temperatura em F: "))
# temperatura_c = (temperatura_f - 32)*5/9
# print(f"{temperatura_f:.2f} Farenheit equivalem a {temperatura_c:.2f} Celsius")

import copy

def determinante3x3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
          - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
          + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

# Entrada dos coeficientes da matriz A e vetor de termos independentes d
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))
a3 = float(input("a3: "))
b3 = float(input("b3: "))
c3 = float(input("c3: "))
d1 = float(input("d1: "))
d2 = float(input("d2: "))
d3 = float(input("d3: "))

# Matriz principal A
A = [[a1, b1, c1],
     [a2, b2, c2],
     [a3, b3, c3]]

# Vetor de termos independentes
d = [d1, d2, d3]

# Criando cópias profundas das matrizes para Dx, Dy, Dz
Dx = copy.deepcopy(A)
Dy = copy.deepcopy(A)
Dz = copy.deepcopy(A)

# Substituindo as colunas apropriadas pelas entradas de d
for i in range(3):
    Dx[i][0] = d[i]
    Dy[i][1] = d[i]
    Dz[i][2] = d[i]

# Calculando os determinantes
D = determinante3x3(A)
Dx_val = determinante3x3(Dx)
Dy_val = determinante3x3(Dy)
Dz_val = determinante3x3(Dz)

# Verificação e saída
if D != 0:
    x = Dx_val / D
    y = Dy_val / D
    z = Dz_val / D
    print(f"A solução única do sistema é <{x:.2f}, <{y:.2f}, <{z:.2f}>")
else:
    print("O sistema não possui solução única")
