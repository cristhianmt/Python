"""
well begin building teh windw, later, well draw the game elements such a ship
and the alien and well also our game respond to user input, set the background color, and load a ship image
"""

"Creating a Pygame windows and responding to usr input"
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.settings.screen_height = self.screen.get_rect().height
        """

        self.screen = pygame.display.set_mode(              # 2.2 When we create a screen we use the screen_width and screen_height attributes of self.settings
            (self.settings.screen_width, self.settings.screen_height)
        )

        """self.screen = pygame.display.set_mode((1100,500))   # 2 dimensions of the game windows"""
        pygame.display.set_caption("Alien invasion")

        # Creaate an instance to store game statistics
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)                              # 1.3 we import ship an then make an instance of ship after the screen has been created
        self.bullets = pygame.sprite.Group()                # 1.14 storing bullets in group
        self.aliens = pygame.sprite.Group()                  # 1.19 We create a group to hold the fleet of aliens, and we call _create_fleet()

        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, "Play")



    def run_game(self):
        """Star the main loop for the game."""
        while True:                                         # 3 event to prssing a key o moving the mouse
            self._check_events()                            # 1.4 We call the method from inside the while loop in run_game().

            if self.stats.game_active:
                self.ship.update()                              # 1.8 add update from ship
                self._update_bullets()                          # 2.18 The code for _update_bullets() is cut and pasted from run_game();
                self._update_aliens()                           # 1.24  We set the aliens’ positions to date

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                """Start a new game when the player clicks Play."""
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):                 # 1.10 refactoring _check events
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to right
            self.ship.moving_right = True                   # 2.6 if the arrow key was pressed we move the ship to right one pixel

        elif event.key == pygame.K_LEFT:                    # 1.9 pygame detects a KEYDOWN to  move the ship to right
            # Move the ship to left
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:                      # 1.13 pygame detects a KEYDOWN to  move the ship to up
            #Move the ship to up
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:                    # 2.13 pygame detects a KEYDOWN to  move the ship to down
            # Move the ship to down
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:                   # 2.15 call _fire_bullet() when the space bar is passed
            self._fire_bullet()

        elif event.key == pygame.K_q:                       # 1.11 pressing Q t quit
            sys.exit()

    def _check_keyup_events(self, event):  # 2.10 refactoring _check events
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # 1.7 modified stop the ship move to right when dont press the key

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  # 2.9 stop the ship move to left when dont press the key

        elif event.key == pygame.K_UP:  # 3.13 stop the ship move to up when dont press the key
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:  # 4.13 stop the ship move to down when dont press the key
            self.ship.moving_down = False





    def _fire_bullet(self):                                     # 3.15 we make an instance of Bullet and call it new_bullet
        """Create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:    # 1.17 limits the player to three bullets at a time
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                        # 4.15 add it to the group bullets using the add()


    def _update_bullets(self):                                  # 1.18 we organized to a separate method
        """Update position of bullets and get rid of old bullets"""
        #Update bullets positions
        self.bullets.update()  # 2.14 update the position of the bullets

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():                      # 1.16 we copy to set up the for loop
            if bullet.rect.bottom <= 0:                         # 2.16 We check each bullet to see whether it has disappeared off the top of the screen
                self.bullets.remove(bullet)                     # 3.16 If it has, we remove it from bullets
        print(len(self.bullets))                                # 4.16 we insert a print() call to show how many bullets currently exist in the game and verify that they’re being deleted

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to bullets-aline collisioin"""
        # 1.25Check for any bullets that have hit aliens
        # if so , get red of bullet and the alien
        # Remove any bullets and alien that have collied
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:  # 1.26 check if the aliens group is empty
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):  # 1.24  We set the aliens’ positions to date

        """Check if the fleet is at an edge,
        the update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        """Update the positions of all aliens in the fleet"""
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Shit hit!!")

        # Look for alien hitting the bottom of the screen
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """Check if any aliens have reaches the botto of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break



    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(False)

    def _create_fleet(self):                                                  # 1.20 Create a methot to make an alien
        """Create the fleet of aliens"""
        # Create an alien and finf the number of alien in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size                         # 1.23 we use the attribute size which contains a tuple with the width and height of a rect object.
        # To figure out how many aliens fit in a row, let’s look at how much horizontal space we have
        available_space_x = self.settings.screen_width - (2 * alien_width)  # 1.21 find the number of alien in a row
        # set the spacing between aliens
        number_alien_x = available_space_x // (2 * alien_width)             # 2.21 set the spacing between aliens

        #Determine the number of rows of aline that fit in the scrren
        ship_height = self.ship.rect.height

        # 2.23 To determine the number of rows, we find the available vertical space by subtracting the alien height
        # from the top, the ship height from the bottom, and two alien heights from the bottom of the screen
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)

        # 3.23  To find the number of rows, we divide the available space by two times the height of an alien.
        # We use floor division because we can only make an integer number of rows.
        number_rows = available_space_y // (2 * alien_height)


        #Create the fulll row of alien
        for row_number in range(number_rows):                   # 4.23 To create multiple rows, we use two nested loops: one outer and one inner loop
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)                                # 1.22 refactoring the code



    def _create_alien(self, alien_number, row_number):                                  # 1.22 refactorin the code
        """Create an alien and place it in the row"""
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size                                      # 1.22 refactoring the code
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():                          # 1.25 If check_edges() returns True, we know an alien is at an edge and the whole fleet needs to change direction
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Update images on the screen, and flip  to the nex screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)                     # 2.1 fill(llenar) the screen with the background using fill()
        self.ship.blitme()                                  # 2.3 after filling the background, we drawthi ship on the screen by calling ship.blitme()
        for bullet in self.bullets.sprites():               # 5.15 draw all fired bullets to the screen
            bullet.draw_bullet()

        self.aliens.draw(self.screen)                        # 2.20 make the alien appear on the screen

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

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
# 4.13 stop the ship move to donw when dont press the key


# 1.14 storing bullets in group
# 2.14 update the position of the bullets

# 1.15 import the bullet
# 2.15 call _fire_bullet() when the space bar is passed
# 3.15 we make an instance of Bullet and call it new_bullet
# 4.15 add it to the group bullets using the add()
# 5.15 draw all fired bullets to the screen bullet


The bullets actually continue to exist;  This is a problem, because they continue to consume memory and
processing power to remove 
# 1.16 we copy to set up the for loop
# 2.16 We check each bullet to see whether it has disappeared off the top of the screen
# 3.16 If it has, we remove it from bullets
# 4.16 we insert a print() call to show how many bullets currently exist in the game and verify that they’re being deleted

# 1.17 limits the player to three bullets at a time

# 1.18 we organized to a separate method
# 2.18 The code for _update_bullets() is cut and pasted from run_game();
 
# 1.19 We create a group to hold the fleet of aliens, and we call _create_fleet()
 
# 1.20 Create a methot to make an alien  
# 2.20 make the alien appear on the screen

# 1.21 find the number of alien in a row
# 2.21 set the spacing between aliens

# 1.22 refactoring the code 


# 1.23 we use the attribute size which contains a tuple with the width and height of a rect object.
# 2.23 To determine the number of rows, we find the available vertical space by subtracting the alien height from 
the top, the ship height from the bottom, and two alien heights from the bottom of the screen
# 3.23  To find the number of rows, we divide the available space by two times the height of an alien. 
We use floor division because we can only make an integer number of rows.
# 4.23 To create multiple rows, we use two nested loops: one outer and one inner loop


# 1.24  We set the aliens’ positions to date


# 1.25Check for any bullets that have hit aliens

# 1.26 check if the aliens group is empty 

"""
