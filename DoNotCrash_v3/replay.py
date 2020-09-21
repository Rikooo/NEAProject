import pygame


class Replay(pygame.sprite.Sprite):
    """ Handles all the car replays """

    def __init__(self, image, pos=None):
        # Used to update replay ghost cars
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.pos = pygame.Vector2(0, 0)

        self.rect = image.get_rect(center=self.pos)
        self.rect = self.rect.inflate(0, -25)

    def update(self):
        """ Used to update the hitbox position for hitbox collision"""

        self.rect.center = self.pos

    def isCollided(self, sprite):

        return self.rect.colliderect(sprite.rect)

    def removeFromSpriteList(self):
        """Used to update sprite group"""

        self.kill()
