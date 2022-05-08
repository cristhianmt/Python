"""
13-2. Better Stars: You can make a more realistic star pattern by introducing
randomness when you place each star. Recall that you can get a random number
like this:
from random import randint
random_number = randint(-10, 10)
This code returns a random integer between −10 and 10. Using your code
in Exercise 13-1, adjust each star’s position by a random amount.
"""
import sys
import pygame
from random import randint

from settings import Settings
from star import Star

class Alien():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        star = Star(self)


        star_width , star_height = star.rect.size

        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (1 * star_width)

        available_space_y = (self.settings.screen_height - (2 * star_height))
        number_rows =  available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
            random_number = randint(-10, 10)

            star = Star(self)
            star_width, star_height = star.rect.size
            star.x = random_number * star_width + 2 * star_width * star_number
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * row_number
            self.stars.add(star)



    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ai = Alien()
    ai.run_game()