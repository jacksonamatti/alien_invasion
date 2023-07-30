import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''uma classe que administrab os porjeteis disparados pela spaconave '''
    def __init__(self,ai_settings, screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #armazena a posicao do projetil como um valor decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullets_speed_factor
        
    def update(self):
            """move o projétil para cima na tela"""
            #atualiza a posição decimal do projétil em y
            self.y -= self.speed_factor
            #atualiza a posicaoa de rect
            self.rect.y = self.y
    def draw_bullets(self):
            """desenha o projétil na tela"""
            pygame.draw.rect(self.screen, self.color, self.rect)