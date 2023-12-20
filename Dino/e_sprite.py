import pygame

def secactus(self):
    if self.tamanho_ya == 70:
        return pygame.image.load("sprites/Cactus/Cactus1.png")
    elif self.tamanho_ya == 100:
        return pygame.image.load("sprites/Cactus/Cactus2.png")
    elif self.tamanho_ya == 115:
        return pygame.image.load("sprites/Cactus/Cactus3.png")