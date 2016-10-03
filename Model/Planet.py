__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Planet:

    def __init__(self, x_pos, y_pos, image):
        self.x = x_pos
        self.y = y_pos
        self.sprite = image

    def draw(self, bg):
        bg.blit(self.sprite, (int(self.x), int(self.y)))
