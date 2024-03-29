import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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


    
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #if mouse is clicked on play button game starts else game does'nt start
        button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked and not stats.game_active:
            #reset game settings
            ai_settings.initialize_dynamic_settings() 
            #hide mouse cursor
            pygame.mouse.set_visible(False)
            stats.reset_stats()
            stats.game_active = True

            #reset scoreboard images
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()
        
            #empty list of aliens and bullets
            aliens.empty()
            bullets.empty()

            #create a new fleet and center the ship
            create_fleet(ai_settings,screen,ship,aliens)
            ship.center_ship()



        

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):

    screen.fill(ai_settings.bg_color)    #background color
    sb.show_score()                      #draw score info

    for bullet in bullets.sprites():
        bullet.draw_bullet()             #redraw all bullets behind ships and aliens
    ship.blitme()                        #drawing image on screen
    aliens.draw(screen)                      #drawing alien on screen


    if not stats.game_active:
        play_button.draw_button()          #draw play button only ig game is inactive


    pygame.display.flip()                #make most recently drawn screen visible





def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
        bullets.update()            #update bullets position

        for bullet in bullets.copy():          #get rid of old bullets 
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)



def check_high_score(stats,sb):
    #check if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()




def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #check if bullets hit aliens if so get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) 

        if len(aliens) == 0:
            #if entire fleet is destroyed empty the bullets and create new fleet
            ai_settings.increase_speed()
            bullets.empty()
            #increase level
            stats.level+=1
            sb.prep_level()
            create_fleet(ai_settings,screen,ship,aliens)
        

        if collisions:
            for aliens in collisions.values():   
                stats.score +=ai_settings.alien_points*len(aliens)                     #in collisions dictionary each value is list of aliens hit by single bullet
                sb.prep_score()
            check_high_score(stats,sb)



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
        


def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1




def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    if stats.ships_left>0:
        #decrement ships left
        stats.ships_left-=1
        #update scorecard
        sb.prep_ships()
        #empty aliens and bullets
        bullets.empty()
        aliens.empty()
        #create a new fleet and put the ship in center
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #pause
        sleep(3)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)




def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break



def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    #update positions of all aliens in fleet
    check_fleet_edges(ai_settings,aliens)
    aliens.update()  
    #looking for alien ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
    #when aliens touch screen this gets executed
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)
    
