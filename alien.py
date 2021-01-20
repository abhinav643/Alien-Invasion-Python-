import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #loading alien image and setting it's rect attribute
        self.image = pygame.image.load('C:\\Users\\ABHINAV\\Desktop\\alien invasion project\\images\\alien.bmp')
        self.rect = self.image.get_rect()

        #starting each new alien at top left corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #storing correct position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        #draw alien at it's location
        self.screen.blit(self.image,self.rect)



    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:            #in this case alien touches right edge
            return True
        elif self.rect.left<=0:                       #alien touches left edge
            return True

    def update(self):
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x


        
