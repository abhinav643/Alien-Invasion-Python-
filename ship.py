import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        #initialize ship and set its starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings     #using ai_settings as an attribute 

        self.image = pygame.image.load('C:\\Users\\ABHINAV\\Desktop\\alien invasion project\\images\\ships.bmp') #to load the ship image
        self.rect =  self.image.get_rect()           #rect object of image
        self.screen_rect = screen.get_rect()        #rect object of screen

        #start each new ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx   
        self.rect.bottom = self.screen_rect.bottom


        self.center = float(self.rect.centerx)           #rect attribute does not hold float values so it is assigned to another variable

        self.moving_right = False                    #movement flag (right)
        self.moving_left = False                     #movement flag (left)



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:     #updating ship movement based on movement flag if it is true moves to right until right arrow key is released
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center-=self.ai_settings.ship_speed_factor         #updating ship movement based on movement flag if it is true moves to left until left arrow key is released

        self.rect.centerx = self.center               #update rect object from self.center variable but takes only int part


    def blitme(self):
        #draw ship at its current location
        self.screen.blit(self.image,self.rect)
    

    def center_ship(self):
        self.center = self.screen_rect.centerx         #placing ship on center of screen 

    
