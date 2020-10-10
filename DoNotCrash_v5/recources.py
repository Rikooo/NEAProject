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
LIGHT_GREEN = (57, 255, 20)
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
car_outline_rectangle_image = pygame.transform.scale(
    right_rectangle_image_raw, (350, 450))
car_outline_selected_image_raw = pygame.image.load(
    path+'/External Files/rectangle_blue.png').convert_alpha()
car_outline_selected_image = pygame.transform.scale(
    car_outline_selected_image_raw, (350, 450))

# Cars ---------------------------------------------------------------------------------#
# Test  Car
car_sprite_raw = pygame.image.load(
    path+'/External Files/test_sprite.png').convert_alpha()
car_sprite = pygame.transform.scale(car_sprite_raw, (40, 58))  # 40, 58
enemy_car_sprite_raw = pygame.image.load(
    path+'/External Files/test_sprite_enemy.png').convert_alpha()
enemy_sprite = pygame.transform.scale(enemy_car_sprite_raw, (40, 58))

# The Classic
the_classic_icon_raw = pygame.image.load(
    path+'/External Files/the_classic_icon.png').convert_alpha()
the_classic_icon = pygame.transform.scale(the_classic_icon_raw, (500, 300))
the_classic_image = pygame.image.load(
    path+'/External Files/the_classic.png').convert_alpha()
the_classic_sprite = pygame.transform.scale(the_classic_image, (50, 40))
the_classic_ghost_sprite_raw = pygame.image.load(
    path+'/External Files/the_classic_ghost.png').convert_alpha()
the_classic_ghost_sprite = pygame.transform.scale(
    the_classic_ghost_sprite_raw, (50, 40))

# The Destroyer
the_destroyer_icon_raw = pygame.image.load(
    path+'/External Files/the_destroyer_icon.png').convert_alpha()
the_destroyer_icon = pygame.transform.scale(the_destroyer_icon_raw, (400, 200))
the_destroyer_image = pygame.image.load(
    path+'/External Files/the_destroyer.png').convert_alpha()
the_destroyer_sprite = pygame.transform.scale(the_destroyer_image, (60, 50))
the_destroyer_ghost_sprite_raw = pygame.image.load(
    path+'/External Files/the_destroyer_ghost.png').convert_alpha()
the_destroyer_ghost_sprite = pygame.transform.scale(
    the_destroyer_ghost_sprite_raw, (60, 50))

# Powerup  -----------------------------------------------------------------------------#
heart_powerup_image = pygame.image.load(
    path+'/External Files/heart_powerup.png').convert_alpha()
speedup_powerup_image = pygame.image.load(
    path+'/External Files/speedup_powerup.png').convert_alpha()
slowdown_powerup_image = pygame.image.load(
    path+'/External Files/slowdown_powerup.png').convert_alpha()
shield_powerup_image = pygame.image.load(
    path+'/External Files/shield_powerup.png').convert_alpha()
reverse_replay_powerup_image = pygame.image.load(
    path+'/External Files/reverse_replay_powerup.png').convert_alpha()
show_route_powerup_image = pygame.image.load(
    path+'/External Files/show_route_powerup.png').convert_alpha()

# Spawn Locations
power_up_recs = [[1200, 200, 50, 50],
                 [270, 560, 50, 50],
                 [800, 400, 50, 50]]
# List of all my powerup images
list_of_powerups = [heart_powerup_image,
                    speedup_powerup_image,
                    slowdown_powerup_image,
                    shield_powerup_image,
                    reverse_replay_powerup_image,
                    show_route_powerup_image]


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
