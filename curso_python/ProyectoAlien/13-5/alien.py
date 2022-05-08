import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):

    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):

        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect( )

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y

        # Store the alien's exact horizontal position.

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y +=(self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y