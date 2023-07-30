import pygame
from settings import Settings
from ship import Ship
import game_function as gf # usando o 'as' que siginifica um apelido para a funcao
from pygame.sprite import Group

def run_game():
    #inicaliza o jogo e cria o objeto tela 
    pygame.init()
    ai_settings = Settings() # aqui esta armazenado as configuracoes 
    screen = pygame.display.set_mode((
        ai_settings.scree_width, ai_settings.screen_height
        )) #cria a janela de exibição
    pygame.display.set_caption("invasao alien ")
    ship = Ship(ai_settings, screen) # cria uma escaçonave
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings,screen,ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen,ship, bullets)
run_game()
    