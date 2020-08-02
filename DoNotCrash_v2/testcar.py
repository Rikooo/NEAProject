from main import *
from car import *
from recources import *


import pygame
from pygame import Vector2
import os
import math


class Test_Car(Car):
    '''Test class to get the basic functionality of the car working'''

    def __init__(self, x_pos=0, y_pos=0):
        self.car_name = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = 90  # Starts facing "North"
        self.turning = 0.0

        # Only need to deal with horizontal component since the game doesn't involve any trajectories
        self.vel = Vector2(0, 0)  # In ms^-1
        self.pos = Vector2(self.x_pos, self.y_pos)
        self.max_vel = 30  # In ms^-1
        self.accel = 1.0  # In ms^-2

    def accelerate(self, dt):  # dt argument passed in from main.py
        """ Accelerates Car from  0 to max_vel """

        if self.vel.x >= self.max_vel:
            self.vel.x = self.vel.x
            self.accel = 0
        else:
            self.vel.x += (self.accel * dt)
            self.accel += 1 * dt

    def steering(self, car_sprite, dt):
        """ Handles Turning support """

        car_length = car_sprite.get_width()
        if self.turning > 20 or self.turning < -20:  # Stops the game from imploding when exceeding max turning angle
            self.turning = 0
        try:
            # math.sin only accepts radians
            turning_rad = car_length / math.sin(math.radians(self.turning))
            angular_vel = self.vel.x / turning_rad

            self.angle += math.degrees(angular_vel) * dt

        except ZeroDivisionError:  # Prevents the game from breaking due to self.turning = 0 thus dividing by 0
            turning_rad = 0
            angular_vel = 0

        self.angle += math.degrees(angular_vel) * dt
        self.pos += self.vel.rotate(-self.angle) * dt
