#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from random import randint

import pygame
import sys

from Model.Bullet import Bullet
from Model.Meteor import Meteor
from Model.Planet import Planet
from Model.Spaceship import Spaceship
from View.Window import Window

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "2.0.0"
__email__ = "mllorens@dcc.uchile.cl"


class Controller:
    def __init__(self):
        self.height = 400
        self.width = 500
        self.lives = 3
        self.bullet_speed = 10
        self.meteor_ratio = 45
        self.ticks_counter = 0

        pygame.init()
        self.win = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Earth Defender!')

        ship_image = pygame.image.load(os.path.join("Resources/ship.png"))
        ship_image.convert()
        planet_image = pygame.image.load(os.path.join("Resources/planet.png"))
        planet_image = pygame.transform.scale(planet_image, (self.height, self.height))
        planet_image.convert()

        meteor_1 = pygame.image.load(os.path.join("Resources/Meteors/m1.png"))
        meteor_1.convert()
        meteor_2 = pygame.image.load(os.path.join("Resources/Meteors/m2.png"))
        meteor_2.convert()
        meteor_3 = pygame.image.load(os.path.join("Resources/Meteors/m3.png"))
        meteor_3.convert()
        meteor_4 = pygame.image.load(os.path.join("Resources/Meteors/m4.png"))
        meteor_4.convert()
        meteor_5 = pygame.image.load(os.path.join("Resources/Meteors/m5.png"))
        meteor_5.convert()
        meteor_6 = pygame.image.load(os.path.join("Resources/Meteors/m6.png"))
        meteor_6.convert()

        self.meteors_images = [meteor_1, meteor_2, meteor_3, meteor_4, meteor_5, meteor_6]

        self.planet = Planet((self.width - self.height)/2, self.height * 3/4, planet_image)
        self.ship = Spaceship(self.width/2, self.height * 3/4, ship_image)
        self.meteors = []
        self.bullets = []
        self.window = Window(self.win, self.planet, self.ship, self.bullets, self.meteors)

        self.pew_sound = pygame.mixer.Sound("Resources/laser.wav")
        self.pew_sound.set_volume(0.2)

        pygame.mixer.music.load("Resources/background.mp3")
        pygame.mixer.music.play(-1, 0.0)

    def update(self):
        self.window.clean()
        self.window.draw()

        for bullet in self.bullets:
            bullet.update()
            bullet.set_validity(0 < bullet.get_y() < self.height)

        for meteor in self.meteors:
            meteor.update()
            meteor.set_validity(0 < meteor.get_y() < self.height)
            if meteor.is_valid():
                meteor.set_impact(meteor.get_y() > self.ship.get_y())
            for bullet in self.bullets:
                if bullet.is_valid() and bullet.impact(meteor):
                    bullet.set_validity(False)
                    meteor.set_validity(False)
                    break

        for index in range(len(self.meteors) - 1, -1, -1):
            if self.meteors[index].has_impacted():
                self.lives -= 1
                self.meteors[index].set_impact(False)
                self.meteors[index].set_validity(False)
            if not self.meteors[index].is_valid():
                self.meteors.pop(index)

        for index in range(len(self.bullets) - 1, -1, -1):
            if not self.bullets[index].is_valid():
                self.bullets.pop(index)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= self.width - self.ship.get_ship_width():
                self.ship.set_x(mouse_pos[0])

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pew_sound.play()
                self.bullets.append(Bullet(self.ship.get_x(), self.ship.get_y(), self.bullet_speed))

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if self.lives <= 0:
            print 'GAME OVER'
            pygame.quit()
            sys.exit()

        self.ticks_counter += 1
        if self.ticks_counter >= self.meteor_ratio:
            sprite = self.meteors_images[randint(0, 5)]
            x_position = randint(0, self.width - sprite.get_size()[0])
            self.meteors.append(Meteor(x_position, 0, 5, sprite))
            self.ticks_counter = 0
