"""Creating a setting Class"""

"""store all these values in one place """
class Settings:
    """A class to store all setings for Alien invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (30, 30, 30)
        self.bullet_allowed = 3

        #Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1