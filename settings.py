class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialise game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        # ship speed
        self.ship_speed = 1.5
        # bullet settings
        self.bullet_speed = 1.0  # note that bullet speed is a float not integer
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 1000
