#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Bullet:
    def __init__(self, initial_x, initial_y, speed_x, speed_y):
        self.x = initial_x
        self.y = initial_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.validity = True

    def update(self):
        self.y -= self.speed_y
        self.x += self.speed_x

    def set_validity(self, status):
        self.validity = status

    def is_valid(self):
        return self.validity

    def impact(self, meteor):
        return meteor.get_y() <= self.y <= meteor.get_bound_y() and \
               meteor.get_x() <= self.x <= meteor.get_bound_x()

    def draw(self, bg):
        pygame.draw.rect(bg, (255, 255, 0), (self.x, self.y, 1, self.speed_y))

    def get_y(self):
        return self.y
