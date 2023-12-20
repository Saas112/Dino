import Dino, chao, pygame, cactus
def main(screen, clock, hitboxes):
        dino1 = Dino.Dino()
        cacto1 = cactus.Cacto()
        chao1 = chao.Chao()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    quit()
            dino1.movimentacao() 
            cacto1.movimentacao(dino1)
            chao1.movimentacao()

            dino1.desenhar(screen, hitboxes)
            cacto1.desenhar(screen, hitboxes)
            chao1.desenhar(screen)

            if cacto1.colisao(dino1):
                 return dino1.pontos()

            pygame.display.flip()
            screen.fill((255, 255, 255))
