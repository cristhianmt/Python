"""
13-4. Steady Rain: Modify your code in Exercise 13-3 so when a row of raindrops
disappears off the bottom of the screen, a new row appears at the top of
the screen and begins to fall."""


import sys
import pygame
from random import  randint

from settings import Settings
from raindrop import Raindrop

class Alien():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # cargar la pantalla
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # llamar al grupo de gotas
        self.raindrops = pygame.sprite.Group()

        self._create_fleet()

        # crear un flota de burbujas
    def _create_fleet(self):
        raindrop = Raindrop(self)
        raindrop_width , raindrop_height = raindrop.rect.size

        # determinar cuantas burbujas caben en una fila
        available_space_x = self.settings.screen_width - (2 * raindrop_width)
        number_raindrop_x = available_space_x // (1 * raindrop_width)

        # determinar cuantas burbujas caben en una columna
        available_space_y = (self.settings.screen_height - (2 * raindrop_height))
        number_rows =  available_space_y // (2 * raindrop_height)

        for row_number in range(-2, number_rows):
            for raindrop_number in range(number_raindrop_x):
                self._create_raindrop(raindrop_number, row_number)



        # crear nuevas gotas para cada columna
    def _create_raindrop(self, raindrop_number, row_number):
            random_number =  randint(-10, 10)
            raindrop = Raindrop(self)
            raindrop_width, raindrop_height = raindrop.rect.size
            raindrop.x = random_number * raindrop_width + 2 * raindrop_width * raindrop_number
            raindrop.rect.x = raindrop.x
            raindrop.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
            raindrop.rect.y = raindrop.y
            self.raindrops.add(raindrop)



    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrop()
            self._update_screen()


    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_raindrop(self):
        #actualiza la posicion de las burbujas
        self.raindrops.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ai = Alien()
    ai.run_game()