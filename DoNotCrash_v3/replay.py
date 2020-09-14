import pygame


class Replay(pygame.sprite.Sprite):
    """ Handles all the car replays """

    def __init__(self, image, replay, GAME_DISPLAY, continuous_timer):
        # Used to update replay ghost cars
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        
        # self.pos = pos
        # self.angle = angle

        self.replay = replay
        self.GAME_DISPLAY = GAME_DISPLAY
        self.continuous_timer = continuous_timer

    def update(self):
        # print("A: ", start)
        # Starts with the first dictionary element in the snapshot list and iterates through  everything
        # How2Read: saved_replay([replay_num][snapshot_number]['key'][0/1])
        # print("Work")
        # 
        try:
            for i in range(len(self.replay)):
                for j in range(len(self.replay[i])):
                    #https://subscription.packtpub.com/book/game_development/9781782162865/1/ch01lvl1sec19/drawing-sprites-intermediate
                    # print(len(replay_copy[i]))
                    # > to start from the beginning otherwise it will display the route in reverse (POSSIBLY USE AS A POWERUP?)
                    if self.continuous_timer > self.replay[i][j]['time']:
                        x_pos, y_pos = self.replay[i][j]['position'][0], self.replay[i][j]['position'][1]
                        pos = pygame.Vector2(x_pos, y_pos)
                        center = self.rect.center
                        
                        """shouldn't blit in herem, should do it via the sprite.draw() method which relies on the oposoion of the rectangel"""
                        rotated_image = pygame.transform.rotate(
                            self.image, self.replay[i][j]['angle'])
                        
                        self.rect.x, self.rect.y = self.replay[i][j]['position'][0], self.replay[i][j]['position'][1] 
                        # self.rect = rotated_image.get_rect(center=center)
                        # self.GAME_DISPLAY.blit(
                        #     rotated_image, pos-(rotated_image.get_width() / 2, rotated_image.get_height() / 2))

                        # del self.replay[i][j]

        except IndexError:
            pass
