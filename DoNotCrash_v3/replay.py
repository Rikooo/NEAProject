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

    def update(self, GAME_DISPLAY, saved_replay):
        # rotated_image = pygame.transform.rotate(
        #     self.image, self.angle)
        # GAME_DISPLAY.blit(
        #     rotated_image, self.pos - (rotated_image.get_width() / 2, rotated_image.get_height() / 2))
        # print(self.pos)
        # GAME_DISPLAY.blit(self.image, [50, 50])
        print(len(saved_replay))
        for i in range(len(saved_replay[0])):

            # pos = [saved_replay[i][i]['position']]

            GAME_DISPLAY.blit(self.image, saved_replay[0][i]['position'])
# self.saved_replay([replay_num][snapshot_number]['key'][0/1])
