import pygame
from settings import Settings
from ship import Ship
import game_function as gf # usando o 'as' que siginifica um apelido para a funcao

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
        gf.check_events()
        gf.update_screen(ai_settings, screen,ship)
run_game()
    