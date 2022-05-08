"""
well begin building teh windw, later, well draw the game elements such a ship
and the alien and well also our game respond to user input, set the background color, and load a ship image
"""

"Creating a Pygame windows and responding to usr input"
import sys
import pygame

from settings import Settings
from ship import Ship

print(pygame.ver)
class AlienInvasion:
    """Overall class to manage game asset and behavior"""
    """clase general para administrar activos y comportamiento"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()                                       # 1 initializes the background settings

        self.settings = Settings()                          # 1.2 we create an instance of Settings and assign it to self.settings


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # 1.12 creating a full screem
        self.settings.screen_width = self.screen.get_rect().width        # 2.12 self.screen tell to pygame to find the windows size
        self.settings.screen_height = self.screen.get_rect().height


        self.screen = pygame.display.set_mode(              # 2.2 When we create a screen we use the screen_width and screen_height attributes of self.settings
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1100,500))   # 2 dimensions of the game windows
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)                              # 1.3 we import ship an then make an instance of ship after the screen has been created

        # set the background color                          # 1.1 we assingn this color to self.bg_color
        self.bg_color = ( 230, 230, 230)





    def run_game(self):
        """Star the main loop for the game."""
        while True:                                         # 3 event to prssing a key o moving the mouse
            self._check_events()                            # 1.4 We call the method from inside the while loop in run_game().
            self.ship.update()                              # 1.8 add update from ship
            self._update_screen()                           # 1.5 We call the method from inside the while loop in run_game().






    def _check_events(self):                                # 2.4 we make a new method
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():                    # 4 returns a list of events that have taken of any keyboard or mouse
            if event.type == pygame.QUIT:                   # 5 to exit the game
                sys.exit()

            elif event.type == pygame.KEYDOWN:              # 1.6 pygame detects a KEYDOWN to  move the ship to right
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:                # 3.9 pygame detects a KEYUP to  move the ship to left
                self._check_keyup_events(event)










    def _check_keydown_events(self, event):                 # 1.10 refactoring _check events
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to right
            self.ship.moving_right = True                   # 2.6 if the arrow key was pressed we move the ship to right one pixel

        elif event.key == pygame.K_LEFT:                    # 1.9 pygame detects a KEYDOWN to  move the ship to right
            # Move the dip to left
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:                      # 1.13 pygame detects a KEYDOWN to  move the ship to up
            # Move the ship to up
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:                    # 2.13 pygame detects a KEYDOWN to  move the ship to down
            # Move the ship to down
            self.ship.moving_down = True


        elif event.key == pygame.K_q:                       # 1.11 pressing Q t quit
            sys.exit()





    def _check_keyup_events(self, event):                   # 2.10 refactoring _check events
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False                  # 1.7 modified stop the ship move to right when dont press the key

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False                   # 2.9 stop the ship move to left when dont press the key

        elif event.key == pygame.K_UP:                      # 3.13 stop the ship move to up when dont press the key
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:                    # 4.13 stop the ship move to down when dont press the key
            self.ship.moving_down = False





    def _update_screen(self):
        """Update imags on the screen, and flip  to the nex scren"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)                     # 2.1 fill(llenar) the screen with the background using fill()
        self.ship.blitme()                                  # 2.3 after filling the background, we drawthi ship on the screen by calling ship.blitme()

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

# 1.5 We call the method from inside the while loop in run_game().

# 1.6 pygame detects a KEYDOWN to  move the ship to right
# 2.6 if the arrow key was pressed we move the ship to right one pixel

# 1.7 modified 2.6

# 1.8 add update from ship stop the ship move tho right when dont press the key

# 1.9 pygame detects a KEYDOWN to  move the ship to right
# 2.9 stop the ship move tho left when dont press the key
# 3.9 pygame detects a KEYUP to  move the ship to left

# 1.10 refactoring _check events
# 2.10 refactoring _check events

# 1.11 pressing Q t quit



# 1.12 creating a full screem
# 2.12 self.screen tell to pygame to find the windows size

# 1.13 pygame detects a KEYDOWN to  move the ship to up
# 2.13 pygame detects a KEYDOWN to  move the ship to down
# 3.13 stop the ship move to up when dont press the key
# 4.13 stop the ship move to down when dont press the key    

"""