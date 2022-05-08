"""

12-1. Blue Sky: Make a Pygame window with a blue background.

"""

"""
well begin building teh windw, later, well draw the game elements such a ship
and the alien and well also our game respond to user input, set the background color, and load a ship image
"""

"Creating a Pygame windows and responding to usr input"
import sys
import pygame

from settings_12 import Settings
from image_ano_12_2 import Anonymus

print(pygame.ver)
class AlienInvasion:
    """Overall class to manage game asset and behavior"""
    """clase general para administrar activos y comportamiento"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()                                       # 1 initializes the background settings

        self.settings = Settings()                          # 1.2 we create an instance of Settings and assign it to self.settings

        self.screen = pygame.display.set_mode(              # 2.2 When we create a screen we use the screen_width and screen_height attributes of self.settings
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1100,500))   # 2 dimensions of the game windows
        pygame.display.set_caption("Alien invasion")
        self.ano = Anonymus(self)                           # 1.3 we import ship an then make an instance of ship after the screen has been created

        # set the background color                          # 1.1 we assingn this color to self.bg_color
        self.bg_color = ( 88, 214, 141)


    def run_game(self):
        """Star the main loop for the game."""
        while True:                                         # 3 event to prssing a key o moving the mouse
            self._check_events()                            # 1.4 We call the method from inside the while loop in run_game().
            self._update_screen()                           # 1.5 We call the method from inside the while loop in run_game().



    def _check_events(self):                                # 2.4 we make a new method
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():                    # 4 returns a list of events that have taken of any keyboard or mouse
            if event.type == pygame.QUIT:                   # 5 to exit the game
                sys.exit()

    def _update_screen(self):
        """Update imags on the screen, and flip  to the nex scren"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)                     # 2.1 fill(llenar) the screen with the background using fill()
        self.ano.blitme()                                   # 2.3 after filling the background, we drawthi ship on the screen by calling ship.blitme()

        # Make the most recently dram screen visible
        pygame.display.flip()                               # 6 update the display to show new positions of game


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


"""
# 1 initializes the background settings
# 2 dimensions of the game windows
# 3 event to prssing a key o moving the mouse
# 4 returns a list of events that have taken of any keyboard or mause
# 5 to exit the game
# 6 update the display to show new positions of game

# 1.1 we assingn this color to self.bg_color
# 2.1 fill(llenar) the screen with the background using fill()

# 1.2 we create an instance of Settings and assign it to self.settings
# 2.2 When we create a screen we use the screen_width and screen_height attributes of self.settings

# 1.3 we import ship an then make an instance of ship after the screen has been created
# 2.3 after filling the background, we drawthi ship on the screen by calling ship.blitme()

# 1.4 We call the method from inside the while loop in run_game().
# 2.4 we make a new method

# 1.5 

"""