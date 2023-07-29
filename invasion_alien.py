import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #inicaliza o jogo e cria o objeto tela 
    pygame.init()
    ai_settings = Settings() # instancia o arquivo settings para poder usar 
    screen = pygame.display.set_mode((
        ai_settings.scree_width, ai_settings.screen_height
        )) #cria a janela de exibição
    pygame.display.set_caption("invasao alien ")
    ship = Ship(screen) # cria uma escaçonave
    
    while True:
        screen.fill(ai_settings.bg_color) #define a cor da tela
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.flip()
run_game()
    