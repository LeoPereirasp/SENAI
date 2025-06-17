# Exercício 1
raio = float(input("Informe o raio: "))
pi = 3.14
area = pi * (raio ** 2)
perimetro = 2 * pi * raio
diametro = 2 * raio
print(f"Cálculo da área:{area}")
print(f"Cálculo do perímetro:{perimetro}")
print(f"Cálculo do diâmetro:{diametro}")

# Exercício 2
celsius = float(input("Informe a temperatura em Celsius: "))
farenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
print(f"Temperatura em Farenheit:{farenheit:.2f}")
print(f"Temperatura em Kelvin:{kelvin:.2f}")

# Exercício 3
nota1 = float(input("Informe a nota do Primeiro Bimestre: "))
nota2= float(input("Informe a nota do Segundo Bimestre: "))
nota3= float(input("Informe a nota do Terceiro Bimestre: "))
nota4= float(input("Informe a nota do Quarto Bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Sua média final é de: {media:.2f} pontos.")