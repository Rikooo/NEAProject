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

    def update(self, GAME_DISPLAY, replay_copy, timer, start):
        # print("A: ", start)
        # Starts with the first dictionary element in the snapshot list and iterates through  everything
        # How2Read: saved_replay([replay_num][snapshot_number]['key'][0/1])

        # self.start = start
        # if self.start:
        #     # print("In start")
        #     # Used so I can remove the last used position to avoid blitting a snake and avoid tampering with my saved data
        #     replay_copy = saved_replay
        #     self.start = False
        print(len(replay_copy))
        for i in range(len(replay_copy)):
            for j in range(len(replay_copy[i])):
                try:
                    print(len(replay_copy[i]))
                    # > to start from the beginning otherwise it will display the route in reverse (POSSIBLY USE AS A POWERUP?)
                    if timer > replay_copy[i][j]['time']:
                        x_pos, y_pos = replay_copy[i][j]['position'][0], replay_copy[i][j]['position'][1]
                        pos = pygame.Vector2(x_pos, y_pos)

                        rotated_image = pygame.transform.rotate(
                            self.image, replay_copy[i][j]['angle'])

                        GAME_DISPLAY.blit(
                            rotated_image, pos-(rotated_image.get_width() / 2, rotated_image.get_height() / 2))
                        # del replay_copy[i][j]

                except IndexError:
                    pass

            # else:
            #     pass
    # def returnStart(self):
    #     return self.start
