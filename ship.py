import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # Carrega a imagem da espaconave
        self.image = pygame.image.load('alien_invasion/images/rocket.bmp')
        # Redimensiona a imagem para ter uma largura de 100 pixels (a altura será ajustada mantendo a proporção original)
        self.image = pygame.transform.scale(self.image, (50, int(self.image.get_height() * (50 / self.image.get_width()))))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela x
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaconave em sua posição atual."""
        self.screen.blit(self.image, self.rect)

        
        