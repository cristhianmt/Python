"""

13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6,
Sideways Shooter. For this exercise, try to develop Sideways Shooter to the
same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make
them move sideways toward the ship. Or, write code that places aliens at random
positions along the right side of the screen and then sends them toward
the ship. Also, write code that makes the aliens disappear when they’re hit.
"""



import sys
import pygame

from settings import Settings
from image import Ship
from bullet import Bullet
from alien import Alien

print(pygame.ver)
class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens =  pygame.sprite.Group()
        self._create_fleet()



    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()



    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    def _check_keydown_events(self, event):

        if event.key == pygame.K_UP:

            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            # Move the ship to down
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()



    def _check_keyup_events(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False



    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()



    def _create_fleet(self):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - (2 * alien_width) - ship_width*3)
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x + 300
        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)



    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break



    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _update_screen(self):
        """Update images on the screen, and flip  to the nex screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Make the most recently dram screen visible
        pygame.display.flip()



    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullets positions
        self.bullets.update()  # 2.14 update the position of the bullets

        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        self._check_bullet_alien_collision()



    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
