import os
import pygame
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
BEIGE = (255, 213, 205)
SALMON = (239, 187, 207)
YELLOW = (255, 213, 126)
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

# Map ----------------------------------------------------------------------------------#
# 1280x720
grass_image = pygame.image.load(
    path+'/External Files/grass_image.png').convert_alpha()
# 1280x720
roads_image = pygame.image.load(
    path+'/External Files/roads.png').convert_alpha()
# 1280x720
lake_image = pygame.image.load(path+'/External Files/lake.png').convert_alpha()
# 1280x720
house_image = pygame.image.load(
    path+'/External Files/house.png').convert_alpha()
# 1280x720
tree_image = pygame.image.load(path+'/External Files/tree.png').convert_alpha()

# Rectangles ---------------------------------------------------------------------------#
middle_rectangle_image = pygame.image.load(
    path+'/External Files/rectangle.png').convert_alpha()
left_rectangle_image_raw = pygame.image.load(
    path+'/External Files/left_rectangle_image.png').convert_alpha()
left_rectangle_image = pygame.transform.scale(
    left_rectangle_image_raw, (150, 55))
right_rectangle_image_raw = pygame.image.load(
    path+'/External Files/right_rectangle_image.png').convert_alpha()
right_rectangle_image = pygame.transform.scale(
    right_rectangle_image_raw, (250, 80))

# Cars ---------------------------------------------------------------------------------#
car_sprite_raw = pygame.image.load(
    path+'/External Files/test_sprite.png').convert_alpha()
car_sprite = pygame.transform.scale(car_sprite_raw, (40, 58))  # 30, 48
enemy_car_sprite_raw = pygame.image.load(
    path+'/External Files/test_sprite_enemy.png').convert_alpha()
enemy_sprite = pygame.transform.scale(enemy_car_sprite_raw, (40, 58))

# Rectangle Definition -----------------------------------------------------------------#
house_rects_list = [(1040, 570, 100, 100),
                    (1040, 425, 100, 100),
                    (250, 440, 100, 100),
                    (250, 615, 100, 100),
                    (1165, 295, 100, 100),
                    (1165, 50, 100, 100)]
trees_rects_list = [(175, 200, 65, 65),
                    (480, 200, 65, 65),
                    (1175, 450, 65, 65),
                    (1175, 575, 65, 65)]

# Health Bar ---------------------------------------------------------------------------#
# 1280x720
red_healthbar_image = pygame.image.load(
    path+'/External Files/red_healthbar.png').convert_alpha()
# 171x25
green_health_image = pygame.image.load(
    path+'/External Files/green_health.png').convert_alpha()
