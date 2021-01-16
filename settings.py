class Settings():
    # a class to store all settings for alien invasion game
    def __init__(self):
        #initialize game's screen setting


        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed_factor = 1.5


        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        #no of bullets allowed at once
        self.bullets_allowed = 3
