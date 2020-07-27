from main import *
from car import *
from misc import *


import pygame
import os
import math


class Test_Car():
    '''Test class to get the basic functionality of the car working'''

    def __init__(self, x_pos=0, y_pos=0, direction=0.0):
        self.car_name = "Test"
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.turn = 0.0  # In degrees
        self.direction = direction
        # Only need to deal with horizontal component since the game doesn't involve any tragectories
        self.vel = 0  # In ms^-1
        self.max_vel = 20.0  # In ms^-1
        self.accel = 30  # In ms^-2
        # In ms^-2 (MIGHT NOT NEED AS USER DOESN'T MANUALLY ACCELERATE)
        self.max_accel = 4.0

    def accelerate(self, dt):  # dt argument passed in main.py
        if self.vel == self.max_vel:  # Prevents further acceleration past maximum velocity
            self.vel = self.vel
        else:
            self.vel += self.accel * dt
        self.x_pos += self.vel * dt

    def getVelocity(self):
        pass

    def getDirection(self):
        pass

    def getPosition(self):
        return (self.x_pos, self.y_pos)

    def calcTurningRad(self):
        pass

    def steering(self):
        pass

    def getSize(self):
        pass

    def getEverything(self):
        pass
        # print("Current Velocity: ", self.velocity)
        # print("X_pos: ", self.x_pos)
        # print(self.y_pos)
