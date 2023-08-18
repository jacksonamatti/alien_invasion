'''CLASSE DE CONFIGURAÇÃO GERAL DO PROJETO'''

class Settings():
    def __init__(self):
        #inicia as configurações do jogo
        
        #configuracao de tela
        self.scree_width = 1200
        self.screen_height = 800
        self.bg_color = (168,168,168)
        self.ship_speed_factor = 1.5
        
        #projeteis
        
        self.bullets_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =  60,60,60
        self.bullets_allowed = 3
        
        