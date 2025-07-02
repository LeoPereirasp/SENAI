import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Clock do jogo
clock = pygame.time.Clock()

# Fonte para pontuação
fonte = pygame.font.SysFont("arial", 40, True, False)

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# Posição inicial da cobra
x_cobra = largura // 2
y_cobra = altura // 2

# Direção inicial da cobra
velocidade = 10
dx = velocidade
dy = 0

# Lista do corpo da cobra
lista_cobra = []
comprimento = 1

# Posição inicial da maçã
x_maca = randint(40, 600)
y_maca = randint(50, 430)

# Pontuação
pontos = 0

# Função para desenhar a cobra
def desenha_cobra(lista):
    for segmento in lista:
        pygame.draw.rect(tela, VERDE, (segmento[0], segmento[1], 20, 20))

# Loop principal do jogo
while True:
    clock.tick(15)
    tela.fill(BRANCO)

    # Mostra pontuação
    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, PRETO)
    tela.blit(texto_formatado, (430, 40))

    # Eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    # Teclas de movimento
    teclas = pygame.key.get_pressed()
    if teclas[K_a] and dx == 0:
        dx = -velocidade
        dy = 0
    if teclas[K_d] and dx == 0:
        dx = velocidade
        dy = 0
    if teclas[K_w] and dy == 0:
        dx = 0
        dy = -velocidade
    if teclas[K_s] and dy == 0:
        dx = 0
        dy = velocidade

    # Atualiza posição da cobra
    x_cobra += dx
    y_cobra += dy

    # Desenha maçã
    maca = pygame.draw.rect(tela, VERMELHO, (x_maca, y_maca, 20, 20))

    # Atualiza corpo da cobra
    cabeca = [x_cobra, y_cobra]
    lista_cobra.append(cabeca)
    if len(lista_cobra) > comprimento:
        del lista_cobra[0]

    # Verifica colisão com a maçã
    if pygame.Rect(x_cobra, y_cobra, 20, 20).colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento += 1

    # Verifica colisão com as bordas
    if x_cobra < 0 or x_cobra > largura - 20 or y_cobra < 0 or y_cobra > altura - 20:
        pygame.quit()
        exit()

    # Verifica colisão com o próprio corpo
    for segmento in lista_cobra[:-1]:
        if segmento == cabeca:
            pygame.quit()
            exit()

    # Desenha a cobra
    desenha_cobra(lista_cobra)

    # Atualiza tela
    pygame.display.update()
