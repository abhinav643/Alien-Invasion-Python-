import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):    #create bullet object at ship's current position
        super().__init__()
        self.screen = screen
        
        
        #creating bullet rect at (0,0) and then set crct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx       #bullet's center to same as ship's center
        self.rect.top = ship.rect.top               #bullet's top to same as ship's top

        #store bullet's position(y cordinate) as decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        self.y-=self.speed_factor      #update decimal position of bullet
        self.rect.y = self.y        #update rect position


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)   #draw.rect method is used to draw a rectangle on window it takes three arguments:screen,color and rect object


    
        
        
        
        


        
        
