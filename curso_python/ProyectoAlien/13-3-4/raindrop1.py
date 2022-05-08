import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings =  ai_game.settings

        # Crgar la imagen
        self.image1 = pygame.image.load('raindrop.png')
        self.image = pygame.transform.scale(self.image1, (55, 49))
        self.rect = self.image.get_rect()

        #poner la imagen en la parte superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # la posición horizontal de cada extraterrestre con precisión
        self.y = float(self.rect.y)


    def update(self):
        #mover las gotas hacia abajo
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y