import math
import pygame
from pygame import Vector2
from car import *


class The_Destroyer(Car, pygame.sprite.Sprite):
    """Test class to get the basic functionality of the car working"""

    def __init__(self, image, x_pos=500, y_pos=0, angle=90):
        # Sprite Functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.car_name = None

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.turning = 0.0

        # Only need to deal with horizontal component since the game doesn't involve any trajectories
        self.vel = Vector2(0, 0)  # In ms^-1
        self.pos = Vector2(self.x_pos, self.y_pos)
        self.max_vel = 14  # In ms^-1
        self.accel = 0.5  # In ms^-2

        # Decreases the length of my rectangle (hitbox) which allows for more accurate real time collision
        self.rect = self.image.get_rect(center=self.pos)
        self.rect = self.rect.inflate(0, 0)

        # self.mask = pygame.mask.from_surface(self.image)
        # self.mask_outline = self.mask.outline()

        # Health
        self.health = 200

    def accelerate(self, dt):  # dt argument passed in from main.py
        """ Accelerates Car from  0 to max_vel """

        if self.vel.x >= self.max_vel:
            self.vel.x = self.vel.x
            self.accel = 0
        else:
            self.vel.x += (self.accel * dt)
            self.accel += 1 * dt

    def steering(self, dt):
        """ Handles Turning support """

        car_length = self.image.get_width()
        if self.turning > 20 or self.turning < -20:  # Stops the game from imploding when exceeding max turning angle
            self.turning = 0
        try:
            # math.sin only accepts radians
            turning_rad = car_length / math.sin(math.radians(self.turning))
            angular_vel = self.vel.x / turning_rad

            self.angle += math.degrees(angular_vel) * dt * 2.5

        except ZeroDivisionError:  # Prevents the game from breaking due to self.turning = 0 thus dividing by 0
            turning_rad = 0
            angular_vel = 0

        self.angle += math.degrees(angular_vel) * dt
        self.pos += self.vel.rotate(-self.angle) * dt

    def update(self):
        """ Updates Rectangle to be in accordance to the images position"""

        self.rect.center = self.pos

    def removeFromSpriteList(self):
        """Used to update sprite group"""

        self.kill()
