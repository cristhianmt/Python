"""
14-1. Press P to Play: Because Alien Invasion uses keyboard input to control
the ship, it would be useful to start the game with a keypress. Add code that
lets the player press P to start. It might help to move some code from _check
_play_button() to a _start_game() method that can be called from _check_play
_button() and _check_keydown_events().
"""



import sys
from time  import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import  Button
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

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens =  pygame.sprite.Group()
        self._create_fleet()

        self.play_button =  Button(self, "Press p to play")




    def run_game(self):

        while True:
            self._check_events()
            if self.stats.game_active:
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

        elif event.key == pygame.K_p:
            self.stats.game_active = True

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
        self._check_aliens_bottom()

    def _check_aliens_botton(self):
        """Check if any aliens have reaches the botto of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break



    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break



    def _change_fleet_direction(self):
        self.settings.fleet_direction *= -1



    def _update_screen(self):
        """Update images on the screen, and flip  to the nex screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
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



    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                # Treat this the same as if the ship got hit
                self._start()
                break



    def _start(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ship_left > 0:
            self.bullets.empty()

            self._create_fleet()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False



if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
