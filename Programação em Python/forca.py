import random

def escolher_palavra():
  """Escolhe uma palavra aleatória de uma lista."""
  palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
  return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
  """Mostra a palavra com letras corretas reveladas e underscores para as restantes."""
  display = ""
  for letra in palavra:
    if letra in letras_corretas:
      display += letra
    else:
      display += "_"
  return display

def jogo_da_forca():
  """Função principal do jogo da forca."""
  palavra_secreta = escolher_palavra()
  letras_corretas = []
  letras_erradas = []
  tentativas = 6

  print("Bem-vindo ao Jogo da Forca!")
  print(mostrar_palavra(palavra_secreta, letras_corretas))

  while tentativas > 0:
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
      print("Por favor, digite apenas uma letra.")
      continue

    if letra in letras_corretas or letra in letras_erradas:
      print("Você já tentou essa letra.")
      continue

    if letra in palavra_secreta:
      letras_corretas.append(letra)
      print("Letra correta!")
    else:
      letras_erradas.append(letra)
      tentativas -= 1
      print(f"Letra errada. Tentativas restantes: {tentativas}")

    print(mostrar_palavra(palavra_secreta, letras_corretas))
    print("Letras erradas:", letras_erradas)

    if "_" not in mostrar_palavra(palavra_secreta, letras_corretas):
      print("Parabéns! Você acertou a palavra:", palavra_secreta)
      return

  print(f"Você perdeu! A palavra era: {palavra_secreta}")

# Iniciar o jogo
jogo_da_forca()