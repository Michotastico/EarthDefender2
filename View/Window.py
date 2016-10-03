import pygame
__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Window:

    def __init__(self, screen, planet, ship, bullets, meteors):
        self.planet = planet
        self.ship = ship
        self.bullets = bullets
        self.meteors = meteors

        self.win = screen
        self.color = (0, 0, 0)

    def clean(self):
        self.win.fill(self.color)

    def draw(self):
        self.planet.draw(self.win)
        self.ship.draw(self.win)
        for bullet in self.bullets:
            bullet.draw(self.win)
        for meteor in self.meteors:
            meteor.draw(self.win)

        pygame.display.flip()
