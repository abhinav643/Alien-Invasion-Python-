class GameStats():
    def __init__(self,ai_settings):
        #initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        #start alien invasion in an inactive state
        self.game_active = False
        #high score should never be reset so write in init method
        self.high_score = 0
    

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        #initialize score in reset_stats so each time game starts score is zero
        self.score = 0
        self.level = 1
        

    
