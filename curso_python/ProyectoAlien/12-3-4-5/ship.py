"""Creating the ship class"""

import pygame
class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen                                # 1
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        #load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')            # 1.2
        self.rect = self.image.get_rect()

        #Star each new ship at the bottom center of the screem
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        #Store a decimal value for ship's vertical position
        self.y = float(self.rect.y)


        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """Update  the ship's position based on the  movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #Update the ship's x value, not the rect
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


            #Update the ship's y value, not the rect
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # Update the ship's y value, not the rect
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed



        # Update rect object from self.x
        self.rect.x = self.x

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)