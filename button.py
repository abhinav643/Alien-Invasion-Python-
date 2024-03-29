import pygame.font
class Button():
    def __init__(self,ai_settings,screen,msg):
        #initialize button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #set dimensions and properties of the Button
        self.width = 200
        self.height = 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)       #none means use default font
        
        #build button's rect object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #button message needs to prep only once
        self.prep_msg(msg)

    def prep_msg(self,msg):
        #turns msg into image and center text on button
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)            #draws rectangular portion of button
        self.screen.blit(self.msg_image,self.msg_image_rect)     #draws text image to the screen
        