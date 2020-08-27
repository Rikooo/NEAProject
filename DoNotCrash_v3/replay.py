import pygame


class Replay(pygame.sprite.Sprite):
    """ Handles all the car replays """

    def __init__(self, image, pos, angle):
        # Used to update replay ghost cars
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.pos = pos
        self.angle = angle

    def update(self):
        # rotated_image = pygame.transform.rotate(self.image, self.angle)
        # self.rect = rotated_image.get_Rect()
        self.rect += 5
