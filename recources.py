import pygame
import os
import json
from main import *


path = os.path.dirname(os.path.dirname(__file__))
path_2 = os.path.dirname(__file__)
print(path)
print(path_2)
# Colours  -----------------------------------------------------------------------------#
ORANGE = (255, 182, 0)
NEON_GREEN = (83, 212, 137)
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
RED = (190, 30, 50)
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

# 1280x720
grass_image = pygame.image.load(
    path+'/External Files/grass_image.png').convert_alpha()


left_rectangle_image_raw = pygame.image.load(
    path+'/External Files/left_rectangle_image.png').convert_alpha()
left_rectangle_image = pygame.transform.scale(
    left_rectangle_image_raw, (150, 55))
right_rectangle_image_raw = pygame.image.load(
    path+'/External Files/right_rectangle_image.png').convert_alpha()
right_rectangle_image = pygame.transform.scale(
    right_rectangle_image_raw, (250, 80))

car_sprite_raw = pygame.image.load(
    path+'/External Files/test_sprite.png').convert_alpha()
car_sprite = pygame.transform.scale(car_sprite_raw, (50, 80))


# Misc  --------------------------------------------------------------------------------#
# Reads the contents of the spawn_points json file
with open(path_2+'/spawn_points.json') as f:  # Automatically a read only file
    spawn_points_list = json.load(f)
