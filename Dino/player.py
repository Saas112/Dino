import pygame

class Dino:
    def __init__(self):
        self.pulo = False
        self.caindo = False
        self.gravidade = 6
        self.x = 100
        self.y = 276
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.altura_do_pulo = 0
        self.pixels_count = 0
        self.font = pygame.font.Font(None, 36)
        self.velocidade = 10

    def pular(self):
        if not self.pulo and not self.caindo and self.y == 276:
            self.pulo = True
            self.altura_do_pulo = 12

    def gravidades(self):
        if self.pulo and self.altura_do_pulo > 0:
            self.y -= 10
            self.altura_do_pulo -= 1
        else:
            self.caindo = True
            if self.y < 276:
                self.y += self.gravidade
            else:
                self.y = 276
                self.pulo = False
                self.caindo = False

        self.rect.y = self.y


    def movimentacao(self):
        keys = pygame.key.get_pressed()
        self.pixels_count += 1
        self.velocidade += 0.001

        if keys[pygame.K_SPACE]:
            self.pular()

        self.gravidades()

    def desenhar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))
        pixels_count_surface = self.font.render(str(self.pixels_count//10), True, (255, 255, 255))
        screen.blit(pixels_count_surface, (550, 10))  