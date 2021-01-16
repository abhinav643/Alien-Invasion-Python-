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

        
