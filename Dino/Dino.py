import pygame, tocamusica

class Dino:
    def __init__(self):
        self.pulo = False
        self.caindo = False
        self.gravidade = 8.5
        self.x = 200
        self.y = 406
        self.p = 0
        self.rect = pygame.Rect(self.x, self.y, 88, 94)
        self.altura_do_pulo = 100
        self.pixels_count = 0
        try:
            self.font = pygame.font.Font(None, 36)
        except: pass
        self.velocidade = 15
        self.sprite1 = pygame.image.load('sprites/T-rex/t-rex-2.png')
        self.sprite2 = pygame.image.load('sprites/T-rex/t-rex-1.png')
        self.sprite_p = pygame.image.load('sprites/T-rex/t-rex-0.png')
        self.triger = 406
        self.sprite_counter = 0
        self.primeiro_pulo  = False

    def pular(self):
        if not self.pulo and not self.caindo and self.y == self.triger:
            tocamusica.Som_pulo()
            self.pulo = True
            self.altura_do_pulo = 19
            self.primeiro_pulo = True

    def gravidades(self):
        if self.pulo and self.altura_do_pulo > 0:
            self.y -= 10
            self.altura_do_pulo -= 1
        else:
            self.caindo = True
            if self.y < self.triger:
                self.y += self.gravidade
            else:
                self.y = self.triger
                self.pulo = False
                self.caindo = False
        self.rect.y = self.y

    def movimentacao(self ):
        keys = pygame.key.get_pressed()
        if self.pixels_count % 10000 == 0:
            self.p += 0.5
        if self.primeiro_pulo:
            self.pixels_count += 1 + self.p
            self.velocidade += 0.001
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.pular()
        self.gravidades()

    def desenhar(self, screen, hitboxes):
        if self.primeiro_pulo:
            if hitboxes == True:
                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 88, 94))
            if self.sprite_counter // 10 % 2 == 0: 
                screen.blit(self.sprite1, (self.x, self.y))
            elif self.y != self.triger:
                screen.blit(self.sprite_p, (self.x, self.y))
            else:
                screen.blit(self.sprite2, (self.x, self.y))
        else:
            screen.blit(self.sprite_p, (self.x, self.y))

        self.sprite_counter += 1
        pixels_count_surface = self.font.render(str(int(self.pixels_count//750)), True, (0,0,0))
        screen.blit(pixels_count_surface, (1150, 10))

    def pontuacao(self):
        with open("point.txt", "a") as f:
            f.write(f"{int(self.pixels_count//750)} \n" )

    def pontos(self):
        return int(self.pixels_count//750)
