# Exercício 1
peso = float(input("Informe seu peso em Kg: "))
altura = float(input("Informe sua altura em m: "))
imc = peso / (altura ** 2)

if imc > 30:
    print("Você está com obesidade!")
elif imc <= 29.9 and imc >= 25:
    print("Você está em sobrepeso!")
elif imc <= 24.9 and imc >= 18.5:
    print("Seu peso está normal")
elif imc < 18.5:
    print("Você está abaixo do peso!")
else:
    pass

# Versão do Professor mais otimizado
# if imc < 18.5:
#     print("Você está abaixo do peso!")
# elif 18.5 <= imc <= 24.9:
#     print("Seu peso está normal")
# elif 24.9 < imc <= 29.9:
#     print("Você está em sobrepeso!")
# else:
#     pass

# Exercício 2
lado_a = float(input("Lado A: "))
lado_b = float(input("Lado B: "))
lado_c = float(input("Lado C: "))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    if lado_a == lado_b == lado_c:
        print("Os lados formam um triângulo equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Os lados formam um triângulo isósceles.")
    else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os valores informados não formam um triângulo.")

# Exercício 3
salario_bruto = float(input("Informe o salário: R$ "))

if salario_bruto <= 2000:
    print("Isento.")
    imposto = 0
elif salario_bruto <= 3500:
    print("Desconto de 10%")
    imposto = salario_bruto * 0.10
elif salario_bruto <= 5000:
    print("Desconto de 15%")
    imposto = salario_bruto * 0.15
else:
    print("Desconto de 20%")
    imposto = salario_bruto * 0.20

salario_liquido = salario_bruto - imposto
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Exercício 4
n1 = float(input("Digite a Nota 1:"))
n2 = float(input("Digite a Nota 2:"))
media = (n1 + n2) / 2

if n1 > 10 or n2 > 10:
    print("Nota Inválida! Por favor informe uma nota de 0 a 10 em ambos os campos!")
elif media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")