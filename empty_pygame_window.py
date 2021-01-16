#import sys
import pygame

from settings import Settings        #class created for settings in game
from ship import Ship                #class created to draw ship image on screen
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()                   #initialize game
    ai_settings = Settings()        #creating object for Settings class
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))   #creating a screen object to draw game's graphical events
    pygame.display.set_caption("alien Invasion")
    ship = Ship(ai_settings,screen)             #creating ship object
    bullets = Group()                           #make a group of bullets to store in
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)  #create a fleet of aliens
    #start main loop for game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
 
