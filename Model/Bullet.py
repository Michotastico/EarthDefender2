#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Bullet:
    def __init__(self, initial_x, initial_y, speed):
        self.x = initial_x
        self.y = initial_y
        self.speed = speed
        self.validity = True

    def update(self):
        self.y -= self.speed

    def set_validity(self, status):
        self.validity = status

    def is_valid(self):
        return self.validity

    def impact(self, meteor):
        return True

    def draw(self, bg):
        pygame.draw.rect(bg, (255, 255, 0), (self.x, self.y, 1, self.speed))

    def get_y(self):
        return self.y
