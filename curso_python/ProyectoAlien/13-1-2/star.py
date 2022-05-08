import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image1 = pygame.image.load('star.png')
        self.image = pygame.transform.scale(self.image1, (55, 49))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


