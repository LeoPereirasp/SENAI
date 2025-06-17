# Operadores de Comparação
"""
== -> Igual a
!= -> Diferente de
 > -> Maior que
 < -> Menor que
>= -> Maior ou Igual a
<= -> Menor ou Igual a
"""

# == -> Igual a
print(10 == 10)
print(10 == 10.0)
print(10 == "10")

# != -> Diferente de
print(10 != 10)
print(10 != 10.0)
print(10 != 2)
print(10 != "10")

# > -> Maior que
print(10 > 10)
print(10 > 10.0)
print(10 > 2)

# < -> Menor que
print(10 < 10)
print(10 < 10.0)
print(10 < 2)

# >= -> Maior ou Igual a
print(10 >= 10)
print(10 >= 10.0)
print(10 >= 2)

# <= -> Menor ou Igual a
print(10 <= 10)
print(10 <= 10.0)
print(10 <= 2)

# Comportamento Booleano dos Dados (bool)
corrida_hoje = 0
print(bool(corrida_hoje))
linhas_escritas = ""
print(bool(linhas_escritas))

# Operadores Lógicos
"""
AND -> E
 OR -> OU
NOT -> NÃO(Negação)
"""

# AND
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print("Thiago" == "thiago" and 10 > 26)
print("Thiago" == "Thiago" and 10 > 26)
print("Thiago" == "Thiago" and 10 < 26)

# OR
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print(10 < 2 or "a" == "a")
print(10 > 2 or "a" == "b")

# Exemplo and e or
# usuario = input("Usuário: ")
# senha = input("Senha: ")
# pin = True
# acesso = usuario == "admin" and senha == "123"
# print(acesso)

# NOT
print(not False)
print(not True)
print(not (10 > 1 and "a" == "b"))

# Exemplo do Reservatório de Água
a = False
b = True
c = True
motor_bomba = ((not a and not b and not c) or (a and not b and not c) or ( a and b and not c))
print(motor_bomba)
print("Ligar Motor!" if motor_bomba else "Motor Desligado!")






