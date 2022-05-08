"""12-6. Sideways Shooter: Write a game that places a ship on the left side of the
screen and allows the player to move the ship up and down. Make the ship fire
a bullet that travels right across the screen when the player presses the spacebar.
Make sure bullets are deleted once they disappear off the screen.
"""

"Creating a Pygame windows and responding to usr input"
import sys
import pygame

from settings import Settings
from image import Ship
from bullet import Bullet

print(pygame.ver)
class AlienInvasion:
    """Overall class to manage game asset and behavior"""
    """clase general para administrar activos y comportamiento"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()                                       # 1 initializes the background settings

        self.settings = Settings()                          # 1.2 we create an instance of Settings and assign it to self.settings


        """self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # 1.12 creating a full screem
        self.settings.screen_width = self.screen.get_rect().width        # 2.12 self.screen tell to pygame to find the windows size
        self.settings.screen_height = self.screen.get_rect().height """


        self.screen = pygame.display.set_mode(              # 2.2 When we create a screen we use the screen_width and screen_height attributes of self.settings
            (self.settings.screen_width, self.settings.screen_height)
        )

        """self.screen = pygame.display.set_mode((1200,800))   # 2 dimensions of the game windows"""
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)                              # 1.3 we import ship an then make an instance of ship after the screen has been created
        self.bullets = pygame.sprite.Group()                # 1.14 storing bullets in group

        """# set the background color                          # 1.1 we assingn this color to self.bg_color
        #self.bg_color = ( 230, 230, 230)"""





    def run_game(self):
        """Star the main loop for the game."""
        while True:                                         # 3 event to prssing a key o moving the mouse
            self._check_events()                            # 1.4 We call the method from inside the while loop in run_game().
            self.ship.update()                              # 1.8 add update from ship
            self._update_bullets()                          # 2.18 The code for _update_bullets() is cut and pasted from run_game();
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

        if event.key == pygame.K_UP:                      # 1.13 pygame detects a KEYDOWN to  move the ship to up
            #Move the ship to up
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:                    # 2.13 pygame detects a KEYDOWN to  move the ship to down
            # Move the ship to down
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:                   # 2.15 call _fire_bullet() when the space bar is passed
            self._fire_bullet()

        elif event.key == pygame.K_q:                       # 1.11 pressing Q t quit
            sys.exit()



    def _check_keyup_events(self, event):                   # 2.10 refactoring _check events

        if event.key == pygame.K_UP:                      # 3.13 stop the ship move to up when dont press the key
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:                    # 4.13 stop the ship move to down when dont press the key
            self.ship.moving_down = False

    def _fire_bullet(self):                                 # 3.15 we make an instance of Bullet and call it new_bullet
        """Create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:    # 1.17 limits the player to three bullets at a time
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                        # 4.15 add it to the group bullets using the add()

    def _update_bullets(self):                                  # 1.18 we organized to a separate method
        """Update position of bullets and get rid of old bullets"""
        #Update bullets positions
        self.bullets.update()  # 2.14 update the position of the bullets

        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():      # 1.16 we copy to set up the for loop
            if bullet.rect.x >= self.settings.screen_width:           # 2.16 We check each bullet to see whether it has disappeared off the top of the screen
                self.bullets.remove(bullet)     # 3.16 If it has, we remove it from bullets
        print(len(self.bullets))                 # 4.16 we insert a print() call to show how many bullets currently exist in the game and verify that they’re being deleted


    def _update_screen(self):
        """Update images on the screen, and flip  to the nex screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)                     # 2.1 fill(llenar) the screen with the background using fill()
        self.ship.blitme()                                  # 2.3 after filling the background, we drawthi ship on the screen by calling ship.blitme()
        for bullet in self.bullets.sprites():               # 5.15 draw all fired bullets to the screen
            bullet.draw_bullet()

        # Make the most recently dram screen visible
        pygame.display.flip()                               # 6 update the display to show new positions of game


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
