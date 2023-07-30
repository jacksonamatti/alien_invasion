import sys 
import pygame
from bullets import Bullet
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
    
    
                    
                        
                    

def update_screen(ai_settings, screen, ship, bullets):
    
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    """Atualiza as balas"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)