import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        '''Inicia o alien e define sua posição atual próxima à parte superior esquerda'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem do alien
        self.image = pygame.image.load('images/estrangeiro.bmp')
        self.image = pygame.transform.scale(self.image, (50, int(self.image.get_height() * (50 / self.image.get_width()))))
        self.rect = self.image.get_rect()
        
        # Define a posição inicial do alien próxima à parte superior esquerda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
