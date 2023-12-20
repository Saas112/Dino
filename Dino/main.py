import pygame, l_principal
from Dino import Dino

def main(): 
    dino = Dino()
    hitboxes = True
    pygame.init() 
    pygame.mixer.init()
    screen = pygame.display.set_mode((1200, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption(f"jogo do Dino")
    try:
        pont = l_principal.main(screen, clock, hitboxes)
    except: pass
    pygame.quit()
    pygame.mixer.quit()
    return pont

if __name__ == "__main__":
    continuar = 's'
    i = 0
    jogadores = {}
    while continuar != 'n':
        i += 1
        
        nome = input(f"Nome do jogador {i}: ")

        pontos = main()
        
        jogadores[nome] = pontos
        print(nome, "fez", pontos, "pontos")

        continuar = input("Continuar? (s/n) ").lower()

        if continuar == 'n':
            for i in jogadores:
                if jogadores[i] == max(jogadores.values()):
                    print(f"\n{i} é o campeão! com {jogadores[i]} pontos\n")
