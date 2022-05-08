"""
12-2. Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen and match the background color of the image to the background
color of the screen, or vice versa.

"""

import pygame
class Anonymus:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        #load the ship image and get its rect.
        self.image = pygame.image.load('image/an.png')
        self.image = pygame.transform.scale(self.image, (55,49))
        self.rect = self.image.get_rect()

        #Star each new ship at the bottom center of the screem
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)