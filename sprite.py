import pygame


class Sprite(pygame.sprite.Sprite):
    """Used for random for mask based collision"""

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.bounding_rects = self.mask.get_bounding_rects()
