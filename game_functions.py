import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True        #move the ship to right continuously
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True         #move the ship to left continuously
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

    elif event.key == pygame.K_q:
        sys.exit()
        

def fire_bullet(ai_settings,screen,ship,bullets):
    #create a new bullet and add it to bullets group
        if len(bullets)<ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:                   #stopping movement of ship after arrow key is released
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False


    
def check_events(ai_settings,screen,ship,bullets):
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            
        elif event.type == pygame.KEYUP:
           check_keyup_events(event,ship)


        

def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)    #background color

    for bullet in bullets.sprites():
        bullet.draw_bullet()             #redraw all bullets behind ships and aliens
    ship.blitme()                        #drawing image on screen
    aliens.draw(screen)                      #drawing alien on screen
    pygame.display.flip()                #make most recently drawn screen visible





def update_bullets(bullets):
        bullets.update()            #update bullets position

        for bullet in bullets.copy():          #get rid of old bullets 
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)


def get_number_aliens_x(ai_settings,alien_width):
    #determine number of aliens that fit in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    #determine number of rows that fit on a screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)             #creating an alien to get it's width
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    

            
def create_fleet(ai_settings,screen,ship,aliens):
    #create a fleet full of aliens
    alien = Alien(ai_settings,screen)           #creating an alien to get it's width
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)


    #create fleet of aliens
    for row_number in range(number_rows):
        #creating first row of aliens
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
    
    