import sys
import pygame

def run_game():
    #inicaliza o jogo e cria o objeto tela 
    pygame.init()
    screen = pygame.display.set_mode((1200,800)) #cria a janela de exibição
    pygame.display.set_caption("invasao alien ")
    bg_color = (230,230,230) # cor de fundo da janela
    
    
    while True:
        #observa eventos do teclado e do mouse
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.flip()
run_game()
    