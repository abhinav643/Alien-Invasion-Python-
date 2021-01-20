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
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        #no of bullets allowed at once
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right , -1 represents left
        
        #how quickly the game speeds up
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()

        #how quickly alien points value increase
        self.score_scale = 1.5


    def initialize_dynamic_settings(self):
        #initialize settings that change through out the game
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # 1 represents right , -1 represents left
        self.alien_points = 50    

    def increase_speed(self):
        self.ship_speed_factor*= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor*= self.speed_scale
        self.alien_points = int (self.alien_points * self.score_scale)

