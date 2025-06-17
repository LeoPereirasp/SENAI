# Exemplo 1
produto = input("Informe um produto (ou enter para sair): ")

if produto:
    quantidade = int(input(f"Informe a quantidade de {produto}: "))
    print(f"""
Produto: {produto}
Quantidade: {quantidade} unidades
""")
else:
    pass

# Exemplo 2
tempo_de_prova = 71

if 50 >= tempo_de_prova > 40:
    print("Próxima Fase.")
elif 70 >= tempo_de_prova > 50:
    print("Repescagem.")
elif tempo_de_prova > 70:
    print("Não classificado!")
else:
    pass