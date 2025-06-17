texto = " PrOgraMação em PYThon "

# Métodos
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.strip().capitalize())
print(texto.strip().replace("em", "com"))

# Métodos de Validação
texto = "#LAT10-A"
email = "thiago@senai.com"
senha = "senha123"
print(texto.startswith("#LIMP"))
print(email.endswith("@senai.com"))
print(senha.isdigit())
print(senha.isalpha())
print(senha.isalnum())

texto = "um teste para a len()"
print(len(texto))

# Strings como iteráveis
# Índice
print(texto[0]) # A primeira opção sempre será 0 na programação
print(texto[3])
print(texto[2])
print(texto[-1]) # A última posição sempre será -1

# Slicing
print(texto[5: 10]) # [inicio: fim]
print(texto[3: 20])
print(texto[3: 50])
print(texto[3: 50: 2]) # vai do 3 ao 50 pulando de 2 em 2
print(texto[:15])
print(texto[5:])
print(texto[::-1])
print("natan"[::-1])





