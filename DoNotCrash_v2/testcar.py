from main import *
from car import *
from misc import *


import pygame
import os
import math


class Test_Car():
    '''Test class to get the basic functionality of the car working'''

    def __init__(self, x_pos=0, y_pos=0):
        self.car_name = "Test"
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.turning_angle = 0.1  # In degrees
        self.angle = 0.0

        # Only need to deal with horizontal component since the game doesn't involve any trajectories
        self.vel = 0.0  # In ms^-1
        self.max_vel = 30.0  # In ms^-1
        self.accel = 1.0  # In ms^-2

    def accelerate(self, dt):  # dt argument passed in main.py

        # Prevents further acceleration past maximum velocity
        if int(self.vel) == int(self.max_vel):
            # self.vel = self.vel
            self.x_pos += self.vel * dt
            # print("MAX VEL REACHED")
        else:
            self.vel += self.accel * dt
            self.x_pos += self.vel * dt
            self.accel += 0.9 * dt

    def getPosition(self):
        return (self.x_pos, self.y_pos)

    def steering(self, car_sprite, dt):
        # print(self.turn)
        turning_rad = car_sprite.get_width() / math.sin(math.radians(self.turning_angle)
                                                        )  # Turns it into rad to make the maths easier
        angular_vel = self.vel / turning_rad  # In s^-1

        self.x_pos += self.vel.rotate(-self.angle) * dt

        self.angle += math.degrees(angular_vel) * \
            dt  # And back into degrees to

    def getLength(self, car_sprite):
        car_length = car_sprite.get_width()  # Used to calculate turning radius
        return car_length

    def getEverything(self):
        pass
        # print("Current Velocity: ", self.velocity)
        # print("X_pos: ", self.x_pos)
        # print(self.y_pos)
