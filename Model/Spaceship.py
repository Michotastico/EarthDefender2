#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Spaceship:
    def __init__(self, x_pos, y_pos, image):
        self.x = x_pos
        self.y = y_pos
        self.sprite = image

    def get_ship_width(self):
        return self.sprite.get_size()[0]

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def get_firing_coord(self):
        return self.x + self.get_ship_width()/2

    def draw(self, bg):
        bg.blit(self.sprite, (int(self.x), int(self.y)))
