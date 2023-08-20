import sys 
import pygame
from bullets import Bullet
from alien import Alien
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keup_events(event, ship)
            

def check_keydown_events(event, ai_settings,screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
            ship.moving_right = True
    elif event.key == pygame.K_q:
                sys.exit()
    elif event.key ==pygame.K_LEFT:
            ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #fire a bullet and add it to the group of bullets
        fire_bullet(ai_settings, screen, ship, bullets)
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            newBullet = Bullet(ai_settings,screen,ship)
            bullets.add(newBullet)
            
            
def check_keup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right= False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    
                    
                        
                    

def update_screen(ai_settings, screen, ship, aliens, bullets):
    
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """Atualiza as balas"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)



def create_fleet(ai_settings, screen, aliens):
    """Cria uma frota de alienígenas na tela."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen,aliens, alien_number)
     




def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.scree_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number):
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number  # Ajuste a posição do alien de acordo com o número
     alien.rect.x = alien.x
     aliens.add(alien)
    
    