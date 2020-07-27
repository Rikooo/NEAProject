import pygame
import os
from main import *


path = os.path.dirname(os.path.dirname(__file__))

# Colours  -----------------------------------------------------------------------------#
ORANGE = (255, 182, 0)
NEON_GREEN = (83, 212, 137)
WHITE = (240, 240, 240)
GREY = (192, 192, 192)
TRANSPARENT = (0, 0, 0, 0)


# Images  ------------------------------------------------------------------------------#

# 1280x720
main_menu_image = pygame.image.load(
    path+'/External Files/main_menu_image.png').convert_alpha()  # Forward slash used to prevent string iterals such as '\a' effecting the code
# 1280x720
choosing_menu_image = pygame.image.load(
    path+'/External Files/choosing_menu_image.png').convert_alpha()
# 32x32
game_icon_image = pygame.image.load(
    path+'/External Files/game_icon_image.png').convert_alpha()
# 64x64
arrow_left_image = pygame.image.load(
    path+'/External Files/arrow_left_image.png').convert_alpha()
# 64x64
arrow_right_image = pygame.image.load(
    path+'/External Files/arrow_right_image.png').convert_alpha()
car_sprite = pygame.image.load(
    path+'/External Files/test_sprite.png').convert_alpha()
