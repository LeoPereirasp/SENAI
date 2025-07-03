from random import randint
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Criando a tela
l = 640
a = 480
tela = pygame.display.set_mode((l, a))

# Nomeando a Janela
pygame.display.set_caption("Sprite")

clock = pygame.time.Clock()

class Cara(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(11):
            self.sprites.append(pygame.image.load(f'attack_{i+1}.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

todas_as_sprites = pygame.sprite.Group()
cara = Cara()
todas_as_sprites.add(cara)

relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    tela.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            cara.atacar()

    chao = pygame.draw.rect(tela, (0, 0, 0), (0, 275, 900, 600))
    alvo = pygame.draw.rect(tela, (255, 0, 0), (2 * l / 3, 180, 50, 50))

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
