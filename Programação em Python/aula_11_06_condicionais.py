"""
 IF  -> Se
ELIF -> Senão se
ELSE -> Senão
"""

# Indentação
"""
Parede
    Nível 1
        Nível 2
"""

codigo_produto = "#1A"
quantidade_produto = 5500

# Contexto 1
if codigo_produto == "#1A":
    if quantidade_produto < 1000:
        print("Quantidade abaixo do mínimo.")
        print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}")
    elif quantidade_produto > 2500:
        print("Quantidade acima do máximo!")
        print(f"Vender {quantidade_produto - 2500} unidade de {codigo_produto} ")
    else:
        print(f"Quantidade de {codigo_produto} ok!")
elif codigo_produto == "#1B":
    if quantidade_produto < 700:
        print("Quantidade abaixo do mínimo.")
        print(f"Comprar {700 - quantidade_produto} unidades de {codigo_produto}")
    elif quantidade_produto > 1500:
        print("Quantidade acima do máximo!")
        print(f"Vender {quantidade_produto - 1500} unidade de {codigo_produto} ")
    else:
        print(f"Quantidade de {codigo_produto} ok!")
else:
    print("Não temos esse produto.")

