import sys
import pygame
from settings import Settings

def run_game():
    #inicaliza o jogo e cria o objeto tela 
    pygame.init()
    ai_settings = Settings() # instancia o arquivo settings para poder usar 
    screen = pygame.display.set_mode((
        ai_settings.scree_width, ai_settings.screen_height
        )) #cria a janela de exibição
    pygame.display.set_caption("invasao alien ")
    
    
    while True:
        #observa eventos do teclado e do mouse
        screen.fill(ai_settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.flip()
run_game()
    