import os
import pygame

path = os.path.dirname(os.path.dirname(__file__))


class Button:
    """ Class Generates a button with text """

    def __init__(self, text, text_colour, text_size, x, y, width, height):
        self.text = text
        self.text_colour = text_colour
        self.text_size = text_size
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, GAME_DISPLAY, rect=None):
        # Need a smaller font to fit into the button
        font = pygame.font.Font(
            path+'/External Files/street.ttf', self.text_size)
        # The actual rectangle 'hitbox' for the button (Transparrent To The User)
        pygame.draw.rect(GAME_DISPLAY, (0, 0, 0),
                         (self.x, self.y, self.width, self.height), -1)
        # -1 sets the width to a negative number thus removing all background and borders from the user
        text_to_button = font.render(self.text, True, self.text_colour)

        # Centres Text by using pygame functions
        GAME_DISPLAY.blit(text_to_button, (self.x + (self.width/2 - text_to_button.get_width()/2),
                                           self.y + (self.height/2 - text_to_button.get_height()/2)))

        if rect is not None:
            GAME_DISPLAY.blit(rect, (self.x, self.y))

    def mouseOver(self, pos):
        # Detects collision with mouse and rectangle
        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True

        return False
