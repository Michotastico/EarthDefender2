#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Meteor:
    def __init__(self, initial_x, initial_y, speed, image):
        self.x = initial_x
        self.y = initial_y
        self.speed = speed
        self.validity = True
        self.impact = False
        self.sprite = image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.y += self.speed

    def set_validity(self, status):
        self.validity = status

    def is_valid(self):
        return self.validity

    def set_impact(self, status):
        self.impact = status

    def has_impacted(self):
        return self.impact

    def draw(self, bg):
        bg.blit(self.sprite, (int(self.x), int(self.y)))

