import pygame


class Replay(pygame.sprite.Sprite):
    """ Handles all the car replays """

    def __init__(self, image, x_pos=500, y_pos=0, angle=90):
        # Used to update replay ghost cars
        pygame.sprite.Sprite.__init__(self)
        self.image = image

        self.replay_time = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle

        self.pos = pygame.Vector2(self.x_pos, self.y_pos)
        self.rect = image.get_rect(center=self.pos)

    def update(self):
        # Starts with the first dictionary element in the snapshot list and iterates through  everything

        self.pos.x, self.pos.y = self.x_pos, self.y_pos
