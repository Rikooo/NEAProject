import pygame
import json
from os import path
from pygame.locals import *
from random import randint
from itertools import repeat
from button import *
from recources import *
from testcar import *
from theclassic import *
from thedestroyer import *
from replay import *
from sprite import *

pygame.init()

# Game Window ----------------------------------------------------------------------------#
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
RES = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
GAME_DISPLAY = pygame.display.set_mode(RES, 0, 32)

path = os.path.dirname(os.path.dirname(__file__))
path_2 = os.path.dirname(__file__)


def displayMessage(text, text_colour, text_size, coords):
    font = pygame.font.Font(
        path+'/External Files/street.ttf', text_size)
    textSurface = font.render(text, False, text_colour)
    GAME_DISPLAY.blit(textSurface, coords)

def playMusic(music_volume):
    # Music
    pygame.mixer.music.play(-1)  # Plays BG song on repeat
    pygame.mixer.music.set_volume(music_volume)
    
    # print(pygame.mixer.music.get_volume())


# # Menu Systems ----------------------------------------------------------------------------#
def mainMenu(music_volume):
    # Individual Menu Buttons                   #Size   x   y  width height
    play_game_button = Button("PLAY GAME", ORANGE, 90, 50, 100, 460, 75)
    choose_car_button = Button("CHOOSE CAR", ORANGE, 75, 80, 220, 400, 65)
    options_button = Button("OPTIONS", ORANGE, 75, 80, 330, 280, 65)
    quit_button = Button("QUIT", ORANGE, 75, 80, 440, 160, 65)
    # Sets music playing
    playMusic(music_volume) # Before options menu is run, default max volume (music_volume on first instance found in recources.py)

    running = True
    while running:
        
        # Displays Background Image First
        GAME_DISPLAY.blit(main_menu_image, (0, 0))
        # Draws Each button to the screen
        play_game_button.draw(GAME_DISPLAY)
        choose_car_button.draw(GAME_DISPLAY)
        options_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.display.quit()
            pygame.quit()
        for event in pygame.event.get():
           # Get's position of mouse to detect collisions
            pos = pygame.mouse.get_pos()
            # Handles quit event
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                # Adds responsiveness to text whewn hovering your mouse over it
                if play_game_button.mouseOver(pos):
                    play_game_button.text_colour, play_game_button.text_size = NEON_GREEN, 100
                elif choose_car_button.mouseOver(pos):
                    choose_car_button.text_colour, choose_car_button.text_size = NEON_GREEN, 85
                elif options_button.mouseOver(pos):
                    options_button.text_colour, options_button.text_size = NEON_GREEN, 85
                elif quit_button.mouseOver(pos):
                    quit_button.text_colour, quit_button.text_size = NEON_GREEN, 85
                else:
                    # When the mouse is not over the buttons, they should return back to their default attributes
                    play_game_button.text_colour, play_game_button.text_size = ORANGE, 90
                    choose_car_button.text_colour, choose_car_button.text_size = ORANGE, 75
                    options_button.text_colour, options_button.text_size = ORANGE, 75
                    quit_button.text_colour, quit_button.text_size = ORANGE, 75

            # HANDLING --------------------------------------------------------------------#
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handles what to do after the user clicks on the corresponding button
                if play_game_button.mouseOver(pos):
                    # This avoids the current state of whatever menu system overriding the intended menu
                    # For example before this, when the user would pause the game and exit to main menu then click play game,
                    # They would immidiately arrive at the pause screen an not the actual game hence the use of a default parameter

                    # Choose same car as previously saved
                    with open(path_2+'/previous_car.txt', 'r') as f:
                        car_choice = int(f.read())
                    Main(initial_run=False, car_choice=car_choice)
                elif choose_car_button.mouseOver(pos):
                    chooseCarMenu()
                elif options_button.mouseOver(pos):
                    optionMenu(music_volume, volume_index)
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

        pygame.display.update()


def chooseCarMenu():
    # Individual Menu Buttons               #Size  x   y  width height
    play_button = Button("Play", NEON_GREEN, 60, 1100, 520, 160, 75)
    main_menu_button = Button("Main Menu", NEON_GREEN, 60, 20, 520, 330, 75)
    quit_button = Button("Quit", NEON_GREEN, 60, 1100, 0, 160, 75)
    left_box_button = Button("", NEON_GREEN, 0, 175, 50, 350, 450)
    right_box_button = Button("", NEON_GREEN, 0, 750, 50, 350, 450)

    running = True
    while running:
        # Displays Background Image First
        GAME_DISPLAY.blit(choosing_menu_image, (0, 0))
        # Draws Each button to the screen
        play_button.draw(GAME_DISPLAY)
        main_menu_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)
        left_box_button.draw(GAME_DISPLAY)
        right_box_button.draw(GAME_DISPLAY)
        GAME_DISPLAY.blit(arrow_left_image, (25, 620))
        GAME_DISPLAY.blit(arrow_right_image, (1150, 620))
        # Rectangles
        GAME_DISPLAY.blit(car_outline_rectangle_image, (175, 50))
        GAME_DISPLAY.blit(car_outline_rectangle_image, (750, 50))
        # Car Objects
        GAME_DISPLAY.blit(the_classic_icon, (150, 60))
        GAME_DISPLAY.blit(the_destroyer_icon, (740, 105))
        # Car Names
        displayMessage("The Classic", YELLOW, 60, (205, 70))
        displayMessage("The Destroyer", YELLOW, 50, (785, 70))
        # Stats
        # -------------------------------------------------------
        displayMessage("HP", WHITE, 50, (210, 270))
        displayMessage("Defence", WHITE, 40, (210, 330))
        displayMessage("Turning Radius", WHITE, 30, (210, 380))
        displayMessage("SPEED", WHITE, 40, (210, 420))

        displayMessage("+ 200", LIGHT_GREEN, 50, (290, 270))
        displayMessage("+ 30", LIGHT_GREEN, 40, (350, 330))
        displayMessage("+ 3.0", LIGHT_GREEN, 30, (420, 380))
        displayMessage("+ 18", LIGHT_GREEN, 40, (320, 420))

        # -------------------------------------------------------
        displayMessage("HP", WHITE, 50, (785, 270))
        displayMessage("Defence", WHITE, 40, (785, 330))
        displayMessage("TURNING RADIUS", WHITE, 30, (785, 380))
        displayMessage("SPEED", WHITE, 40, (785, 420))

        displayMessage("+ 200", LIGHT_GREEN, 50, (865, 270))
        displayMessage("+ 60", LIGHT_GREEN, 40, (925, 330))
        displayMessage("+ 2.5", LIGHT_GREEN, 30, (995, 380))
        displayMessage("+ 14", LIGHT_GREEN, 40, (895, 420))

        for event in pygame.event.get():
           # Get's position of mouse to detect collisions
            pos = pygame.mouse.get_pos()
            # Handles quit event
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                # Adds responsiveness to text whewn hovering your mouse over it
                if play_button.mouseOver(pos):
                    play_button.text_colour, play_button.text_size = ORANGE, 70
                elif main_menu_button.mouseOver(pos):
                    main_menu_button.text_colour, main_menu_button.text_size = ORANGE, 70
                elif quit_button.mouseOver(pos):
                    quit_button.text_colour, quit_button.text_size = ORANGE, 70
                elif left_box_button.mouseOver(pos):
                    GAME_DISPLAY.blit(car_outline_selected_image, (175, 50))
                elif right_box_button.mouseOver(pos):
                    GAME_DISPLAY.blit(car_outline_selected_image, (750, 50))

                else:
                    play_button.text_colour, play_button.text_size = NEON_GREEN, 60
                    main_menu_button.text_colour, main_menu_button.text_size = NEON_GREEN, 60
                    quit_button.text_colour, quit_button.text_size = NEON_GREEN, 60

            # HANDLING --------------------------------------------------------------------#
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handles what to do after the user clicks on the corresponding button
                if play_button.mouseOver(pos):
                    Main(initial_run=False)
                elif main_menu_button.mouseOver(pos):
                    mainMenu(music_volume)
                elif left_box_button.mouseOver(pos):
                    GAME_DISPLAY.blit(car_outline_selected_image, (175, 50))
                    Main(initial_run=False, car_choice=1)
                elif right_box_button.mouseOver(pos):
                    GAME_DISPLAY.blit(car_outline_selected_image, (750, 50))
                    Main(initial_run=False, car_choice=2)
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

        pygame.display.update()


def optionMenu(music_volume, volume_index):

    back_button = Button("Main Menu", ORANGE, 60, 20, 600, 330, 75)
    left_arrow_button = Button("", BLACK, 0, 115, 163, 40, 40)
    right_arrow_button = Button("", BLACK, 0, 451, 163, 40, 40)

    volume_index = 9  # Max volume by default
    # volume = 1.0
    running = True
    while running:
        
        GAME_DISPLAY.fill((NAVY))
        # Controls
        GAME_DISPLAY.blit(car_control_image, (900, 30))
        GAME_DISPLAY.blit(a_key_image, (950, 320))
        GAME_DISPLAY.blit(d_key_image, (1050, 320))
        GAME_DISPLAY.blit(left_key_image, (950, 420))
        GAME_DISPLAY.blit(right_key_image, (1050, 420))
        displayMessage("Powerup Activation:", ORANGE, 40, (880, 550))
        GAME_DISPLAY.blit(space_key_image, (1000, 600))

        # Volume Control
        displayMessage("~- Volume -~", SALMON, 50, (155, 100))
        dots_rects_list = [[160, 175, 15, 15],  # 0.1
                           [190, 175, 15, 15],  # 0.2
                           [220, 175, 15, 15],  # 0.3
                           [250, 175, 15, 15],  # 0.4
                           [280, 175, 15, 15],  # 0.5
                           [310, 175, 15, 15],  # 0.6
                           [340, 175, 15, 15],  # 0.7
                           [370, 175, 15, 15],  # 0.8
                           [400, 175, 15, 15],  # 0.9
                           [430, 175, 15, 15]]  # 1.0

        GAME_DISPLAY.blit(left_arrow_options_image, (120, 167))
        GAME_DISPLAY.blit(right_arrow_options_image, (456, 167))
        display_rects = [pygame.draw.rect(GAME_DISPLAY, WHITE, dots_rects_list[i])
                         for i in range(len(dots_rects_list))]

        try:
            circle_x = dots_rects_list[volume_index][0] + 7
            circle_y = dots_rects_list[volume_index][1] + 8
        except IndexError:
            # Encapsulates error when click the button when already on max volume
            pass

        pygame.draw.circle(GAME_DISPLAY, BLACK, (circle_x, circle_y), 18, 2)

        back_button.draw(GAME_DISPLAY)
        left_arrow_button.draw(GAME_DISPLAY)
        right_arrow_button.draw(GAME_DISPLAY)

        for event in pygame.event.get():
            # Get's position of mouse to detect collisions
            pos = pygame.mouse.get_pos()
            # Handles quit event
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                # Adds responsiveness to text whewn hovering your mouse over it
                if back_button.mouseOver(pos):
                    back_button.text_colour, back_button.text_size = NEON_GREEN, 70
                else:
                    back_button.text_colour, back_button.text_size = ORANGE, 60

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handles what to do after the user clicks on the corresponding button

 
                if back_button.mouseOver(pos):
                    mainMenu(music_volume)
            
                elif left_arrow_button.mouseOver(pos):
                    volume_index -= 1
                    music_volume -= 0.1
                    if volume_index < 0:
                        volume_index = 0
                elif right_arrow_button.mouseOver(pos):
                    volume_index += 1
                    music_volume += 0.1
                    if volume_index > 9:
                        volume_index = 9
                #print(volume_index)

        pygame.display.update()


def pauseMenu():
    # Individual Menu Buttons                 #Size   x   y  width height
    resume_button = Button("Resume Game", ORANGE, 90, 365, 200, 545, 75)
    # Placed Button Left Area
    main_menu_button = Button("Main Menu",
                              ORANGE, 60, 20, 520, 330, 75)
    quit_button = Button("Quit Game", ORANGE, 90, 415, 310, 445, 75)

    running = True
    while running:

        # This will give the "fade" animation
        rect = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
        rect.fill((102, 178, 255, 10))
        GAME_DISPLAY.blit(rect, (0, 0))

        displayMessage("- PAUSED - ", WHITE, 80, (475, 50))

        # Draws Each button to the screen
        resume_button.draw(GAME_DISPLAY)
        main_menu_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)
        GAME_DISPLAY.blit(arrow_left_image, (25, 620))

        for event in pygame.event.get():
            # Get's position of mouse to detect collisions
            pos = pygame.mouse.get_pos()
            # Handles quit event
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                # Adds responsiveness to text whewn hovering your mouse over it
                if resume_button.mouseOver(pos):
                    resume_button.text_colour, resume_button.text_size = NEON_GREEN, 105
                elif main_menu_button.mouseOver(pos):
                    main_menu_button.text_colour, main_menu_button.text_size = NEON_GREEN, 70
                elif quit_button.mouseOver(pos):
                    quit_button.text_colour, quit_button.text_size = NEON_GREEN, 105
                # When the mouse is not over the buttons, they should return back to their default attributes
                else:
                    resume_button.text_colour, resume_button.text_size = ORANGE, 90
                    main_menu_button.text_colour, main_menu_button.text_size = ORANGE, 60
                    quit_button.text_colour, quit_button.text_size = ORANGE, 90

            # HANDLING --------------------------------------------------------------------#
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handles what to do after the user clicks on the corresponding button
                if resume_button.mouseOver(pos):
                    # Returns the user back to the game
                    running = False  # Breaks out of while loop
                    return True  # Breaks out of function
                elif main_menu_button.mouseOver(pos):
                    mainMenu(music_volume)
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Adds a little convinience so if the user wants to return to the game without having to click any buttons they can do so
                if event.key == pygame.K_ESCAPE:
                    running = False  # Breaks out of while loop
                    return True  # Breaks out of function

        pygame.display.update()


def gameOverMenu():
    play_again_button = Button(
        "Play again", NEON_GREEN, 60, 510, 600, 280, 75)
    main_menu_button = Button("Main Menu", NEON_GREEN, 60, 20, 520, 330, 75)
    choose_car_button = Button("Choose Car", NEON_GREEN, 60, 960, 520, 280, 75)
    quit_button = Button("Quit", NEON_GREEN, 60, 1100, 0, 160, 75)
    
    with open(path_2+'/previous_car.txt', 'r') as f:
            car_choice = int(f.read())
            

    running = True
    while running:
        # Fill Background
        GAME_DISPLAY.fill((134, 117, 169))
        # Draws Each button to the screen
        play_again_button.draw(GAME_DISPLAY)
        main_menu_button.draw(GAME_DISPLAY)
        choose_car_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)

        with open(path_2+'/currentscore.txt', 'r') as f:
            current_score = f.read()

        with open(path_2+'/highscore.txt', 'r') as f:
            high_score = f.read()

        # Game over messages
        displayMessage("GAME OVER", RED, 100, (380, 50))
        pygame.draw.rect(GAME_DISPLAY, SALMON, (360, 150, 560, 5))
        displayMessage(
            f"Score: {current_score}", BEIGE, 70, (523, 230))
        displayMessage(
            f"High Score: {high_score}", YELLOW, 70, (435, 320))

        for event in pygame.event.get():
           # Get's position of mouse to detect collisions
            pos = pygame.mouse.get_pos()
            # Handles quit event
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                # Adds responsiveness to text whewn hovering your mouse over it
                if play_again_button.mouseOver(pos):
                    play_again_button.text_colour, play_again_button.text_size = ORANGE, 70
                elif main_menu_button.mouseOver(pos):
                    main_menu_button.text_colour, main_menu_button.text_size = ORANGE, 70
                elif choose_car_button.mouseOver(pos):
                    choose_car_button.text_colour, choose_car_button.text_size = ORANGE, 70
                elif quit_button.mouseOver(pos):
                    quit_button.text_colour, quit_button.text_size = ORANGE, 70
                else:
                    play_again_button.text_colour, play_again_button.text_size = NEON_GREEN, 60
                    main_menu_button.text_colour, main_menu_button.text_size = NEON_GREEN, 60
                    choose_car_button.text_colour, choose_car_button.text_size = NEON_GREEN, 60
                    quit_button.text_colour, quit_button.text_size = NEON_GREEN, 60

            # HANDLING --------------------------------------------------------------------#
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handles what to do after the user clicks on the corresponding button
                if play_again_button.mouseOver(pos):
                    Main(initial_run=False, car_choice=car_choice)
                elif main_menu_button.mouseOver(pos):
                    mainMenu(music_volume)
                elif choose_car_button.mouseOver(pos):
                    chooseCarMenu()
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

        pygame.display.update()


class Main:
    """ Class controls the entire program """

    def __init__(self, initial_run=True, car_choice=1, music_volume=1):
        # Initialisations ----------------------------------------------------------------------#
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Used to run generateSpawnPoint() only once at the start of the turn
        self.flag_spawn = True
        self.spawn_points_list = []

        # 1 = The classic, 2 = The destroyer
        self.car_choice = car_choice

        # Slightly above 'n' to allow the user to react to the timer before counting down
        self.timer = 10.5 # SHOULD BE 10.5
        self.powerup_timer = 3.5  # How Long a power up lasts

        self.turn_count = 1
        self.snapshots = []
        self.saved_replay = []
        self.dt = 0  # (Explained bellow when value is assigned to it)

        # Sprite Handling ----------------------------------------------------------------------#
        self.user_car_sprite = pygame.sprite.Group()
        self.replay_sprites_group = pygame.sprite.Group()

        # Game Window --------------------------------------------------------------------------#
        pygame.display.set_caption('Do Not Crash!')
        pygame.display.set_icon(game_icon_image)

        

        # Objects ------------------------------------------------------------------------------#
        if car_choice == 1:
            self.replay_object = Replay(the_classic_ghost_sprite)
        elif car_choice == 2:
            self.replay_object = Replay(the_destroyer_ghost_sprite)
        else:
            print(car_choice)
            print("Error")
            pygame.display.quit()
            pygame.quit()

        self.lake_object = Sprite(lake_image)

        # Misc  --------------------------------------------------------------------------------#
        self.true_scroll = [0, 0]
        self.screen_shake = 10
        self.player_health = 200

        # Power Up Handling --------------------------------------------------------------------#
        self.health_collected = False
        self.speedeup_collected = False
        self.slowdown_collected = False
        self.shield_collected = False
        self.reverse_collected = False
        self.route_collected = False

        self.speedup_activated = False
        self.slowdown_activated = False
        self.shield_activated = False
        self.reverse_activated = False
        self.route_actived = False

        self.place_powerup = True
        self.powerup_collided = False
        self.replay_reverse = False
        
        self.reverse_turn_activated = False

        # Runs Main Methods --------------------------------------------------------------------#
        self.running = True
        self.initial_run = initial_run
        self.run()

    def run(self):
        # Main game loop

        while self.running:

            if self.initial_run:
                mainMenu(music_volume)  # The function makes initial run = False otherwise the saved state will carry on between menu screens

            if self.flag_spawn == True:
                self.generateSpawnPoint()

            # This allows us to do integration for some physics simulation
            self.dt = self.clock.get_time() / 100

            self.createMap()
            self.createTimer()
            self.handleCar()
            self.saveSnapshot()

            # Checks if the turn count is a multiple of 4 to display powerup
            if self.place_powerup and self.turn_count % 1 == 0:
                loc = randint(0, 2)
                powerup_choice = randint(0, len(list_of_powerups)-1)
                self.no_powerup = False
                self.place_powerup = False

            elif self.turn_count % 1 != 0:
                self.no_powerup = True

            if self.no_powerup:
                pass
            else:
                self.powerUp(loc, 4)

            self.drawHealthBar()
            self.showPowerUp()
            self.events()
            self.update()
  
 
        
    def generateSpawnPoint(self):
        # Generates a location for the car to spawn at

        if self.turn_count == 1:
            # Reads the contents of the spawn_points json file
            # Also resets the spawn_points if the user exits to main menu in the middle of the game
            with open(path_2+'/spawn_points.json') as f:  # Automatically a read only file
                self.spawn_points_list = json.load(f)

        try:  # Encapsulate error when the game runs out of spawn points
            # print(self.spawn_points_list)
            index = randint(0, len(self.spawn_points_list)-1)
            new_spawn_location = self.spawn_points_list[index]
            # Avoids respawning in the same location by deleting the used spawn location index
            
            if self.car_choice == 1:
                self.car = The_Classic(
                    the_classic_sprite, new_spawn_location[0], new_spawn_location[1], new_spawn_location[2])
                self.car.health = self.player_health # Assures cars health is not reset every turn
                
                
            elif self.car_choice == 2:
                self.car = The_Destroyer(
                    the_destroyer_sprite, new_spawn_location[0], new_spawn_location[1], new_spawn_location[2])
                self.car.health = self.player_health # Assures cars health is not reset every turn
            
              
            else:
                print("Error")
                pygame.display.quit()
                pygame.quit()
            
            
  
            
            self.user_car_sprite.add(self.car)
            del self.spawn_points_list[index]
            self.flag_spawn = False
            
            with open(path_2+'\previous_car.txt', 'w') as f:
                f.write(str(self.car_choice))
           
        except ValueError:
            # print("Ran out of spawn points")
            pass

    def createMap(self, x=0, y=0):
        # Handles all objects seen on the map

        # Copy use for shake
        self.scroll = self.true_scroll.copy()

        # x and y used to displace objects after for screen shake effect
        GAME_DISPLAY.blit(grass_image, (x, y))
        GAME_DISPLAY.blit(roads_image, (x, y))
        GAME_DISPLAY.blit(house_image, (x, y))
        GAME_DISPLAY.blit(tree_image, (x, y))
        GAME_DISPLAY.blit(lake_image, (x, y))

        # Transparent Rectangle Behind Turn Count/Timer
        GAME_DISPLAY.blit(left_rectangle_image, (0, 0))
        GAME_DISPLAY.blit(right_rectangle_image, (1080, -25))

        # displayMessage(f"FPS: {int(self.clock.get_fps())}",
        #                WHITE, 20, (50, 100))
        # displayMessage(f"Health: {self.car.health}", RED, 35, (640, 10))

        self.wallTeleport()
        displayMessage(f"Turn: {self.turn_count}", WHITE, 35, (24, 10))

        # Car
        rotated_image = pygame.transform.rotate(
            self.car.image, self.car.angle)
        GAME_DISPLAY.blit(rotated_image, self.car.pos -
                          (rotated_image.get_width() / 2, rotated_image.get_height() / 2))

    def createTimer(self):
        # Timer

        if self.timer < 10.5 and self.timer > 6:
            displayMessage(f"Time: {int(self.timer)}", WHITE, 35, (1100, 10))
        # Turns red when the clock hits 5 seconds to notify the user their turn is nearly over
        elif self.timer <= 6 and self.timer >= 4:
            displayMessage(f"Time: {int(self.timer)}", RED, 35, (1100, 10))
        # Shows ms for the last 3 seconds
        elif self.timer <= 4 and self.timer >= 0:  # Won't realistically hit close to 0 due to lag
            displayMessage(
                f"Time: {self.timer:.2f}", RED, 35, (1100, 10))  # 2 decimal places

        dt = self.dt / 10  # Get's My Time in seconds
        self.timer -= dt

        # Handles everything that should happen at the end of the turn
        if self.timer < 0:
            # Removes the previous turns sprite from the group as it is becomes a 'replay' sprite
            self.car.removeFromSpriteList()
            self.place_powerup = True
            self.powerup_collided = False
            self.timer = 10.5  # Resets timer
            self.saved_replay.append(self.snapshots)
            self.snapshots = []
            self.turn_count += 1
            self.reverse_turn_activated = False

            if len(self.saved_replay) == 3:
                del self.saved_replay[0]

            self.flag_spawn = True

    def handleCar(self):
        # Handles the car logic

        self.car.accelerate(self.dt)
        self.car.steering(self.dt)
        self.car.update()

        if self.player_health <= 0:
            self.saveScore()
            gameOverMenu()

        # Car Replay -----------------------------------------------------------------------#
        if self.turn_count > 1:
            if self.replay_reverse:
                self.displayReplays(reverse=True)
            else:
                self.displayReplays()

        # Power Up -------------------------------------------------------------------------#

        # Car Collision With Objects--------------------------------------------------------#
        # Blits Hitboxes around objects
        # tree_rects = [pygame.draw.rect(GAME_DISPLAY, BLACK, trees_rects_list[i], 2)
        #               for i in range(len(trees_rects_list))]
        # house_rects = [pygame.draw.rect(GAME_DISPLAY, BLACK, house_rects_list[i], 2)
        #                for i in range(len(house_rects_list))]

        house_rects = [house_rects_list[i]
                       for i in range(len(house_rects_list))]
        tree_rects = [trees_rects_list[i]
                      for i in range(len(trees_rects_list))]

        # Collision with car and house/tree
        for i in range(len(house_rects)):
            for x in range(len(tree_rects)):

                if self.car.rect.colliderect(house_rects[i]) or self.car.rect.colliderect(tree_rects[x]):
                    self.screen_shake = 10
                    self.collision()

        # Draws Mask around lake
        # for point in self.lake_object.mask_outline:
        #     self.lake_object.mask_outline[0] = (point[0], point[1])
        # pygame.draw.polygon(GAME_DISPLAY, (0, 0, 0),
        #                     self.lake_object.mask_outline, 3)

        # Collision with lake unless shield powerup is activated
        if self.shield_activated:
            pass
        else:
            for b_rect in self.lake_object.bounding_rects:
                if b_rect.contains(self.car):
                    self.saveScore()
                    gameOverMenu()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:

            if self.health_collected:
                self.healthPowerUp()
                self.health_collected = False

            elif self.speedeup_collected:
                self.speedup_activated = True
                self.powerup_timer = 3.5
                self.speedeup_collected = False

            elif self.slowdown_collected:

                self.slowdown_activated = True
                self.powerup_timer = 3.5
                self.slowdown_collected = False

            elif self.shield_collected:
                self.shield_activated = True
                self.powerup_timer = 3.5
                self.shield_collected = False

            elif self.reverse_collected:
                self.reverse_activated = True
                self.powerup_timer = 3.5
                self.reverse_collected = False

            elif self.route_collected:
                self.route_actived = True
                self.powerup_timer = 3.5
                self.route_collected = False

        if self.speedup_activated:
            self.speedupPowerUp()
        elif self.slowdown_activated:
            self.slowdownPowerUp()
        elif self.shield_activated:
            self.shieldPowerUp()
        elif self.reverse_activated:
            self.reversePowerUp()
        elif self.route_actived:
            self.routePowerUp()

        # Testing -------------------------------------------------------------------------#
        # displayMessage(
        #     f"Current Turning: {self.car.turning}", WHITE, 20, (1000, 450))
        # displayMessage(
        #     f"Current Vel: {self.car.vel}", WHITE, 20, (1000, 500))
        # displayMessage(
        #     f"Current Accel: {self.car.accel}", WHITE, 20, (1000, 600))
        # displayMessage(
        #     f"Current Angle: {self.car.angle}", WHITE, 20, (1000, 550))
        # displayMessage(
        #     f"Current Pos: {self.car.pos}", WHITE, 20, (800, 450))

    def saveSnapshot(self):
        # Records all the essential car movements at a given moment in time

        # Stores the pos and rotation of the car at a given time
        # Time will be in synch with the current time during the round
        data_points = {'time': self.timer,
                       'position': [self.car.pos.x, self.car.pos.y],
                       'angle': self.car.angle}
        self.snapshots.append(data_points)

    def displayReplays(self, reverse=False):
        # Handles everything replay related

        if not reverse and self.reverse_turn_activated == False:   ####1
            # Starts with the first dictionary element in the snapshot list and iterates through  everything
            for i in range(len(self.saved_replay)):
                for j in range(len(self.saved_replay[i])):
                    
                    x_pos = self.saved_replay[i][j]['position'][0]
                    y_pos = self.saved_replay[i][j]['position'][1]
                    angle = self.saved_replay[i][j]['angle']

                    # Synchronises the current time with the replay time to display the replay in real time wuth a varience of ~0.04

                    if self.saved_replay[i][j]['time'] > self.timer and self.saved_replay[i][j]['time'] < self.timer+0.04:
                        pos = pygame.Vector2(x_pos, y_pos)
                        self.replay_object.pos = pos

                        # Draws the hitbox around the replay cars
                        self.replay_object.update()
                        # pygame.draw .rect(GAME_DISPLAY, BLACK,
                        #                   self.replay_object.rect, 2)
                        self.replay_sprites_group.add(self.replay_object)

                        if self.replay_object.isCollided(self.car):
                            # Screen Shake animation to show collision
                            self.screen_shake = 10
                            self.collision()
                        
                        self.j = j # For ###3
                        

                        # Blits the Car to the screen
                        rotated_image = pygame.transform.rotate(
                            self.replay_object.image, angle)
                        GAME_DISPLAY.blit(rotated_image, pos -
                                          (rotated_image.get_width() / 2, rotated_image.get_height() / 2))
                        # breaks out before it can blit more than 1 car in the replay
                        break
        
        if not reverse and self.reverse_turn_activated:
            for i in range(len(self.saved_replay)):
                for j in range(len(self.saved_replay[i])):
                    
                    x_pos = self.saved_replay[i][self.j]['position'][0]
                    y_pos = self.saved_replay[i][self.j]['position'][1]
                    angle = self.saved_replay[i][self.j]['angle']

                    
                    # Synchronises the current time with the replay time to display the replay in real time wuth a varience of ~0.04
                   
                    if self.saved_replay[i][j]['time'] > self.timer and self.saved_replay[i][j]['time'] < self.timer+0.04:
                   
                       
                        pos = pygame.Vector2(x_pos, y_pos)
                        self.replay_object.pos = pos

                        # Draws the hitbox around the replay cars
                        self.replay_object.update()
                        # pygame.draw .rect(GAME_DISPLAY, BLACK,
                        #                   self.replay_object.rect, 2)
                        self.replay_sprites_group.add(self.replay_object)

                        if self.replay_object.isCollided(self.car):
                            # Screen Shake animation to show collision
                            self.screen_shake = 10
                            self.collision()

                        # Blits the Car to the screen
                        rotated_image = pygame.transform.rotate(
                            self.replay_object.image, angle)
                        GAME_DISPLAY.blit(rotated_image, pos -
                                            (rotated_image.get_width() / 2, rotated_image.get_height() / 2))
                        # breaks out before it can blit more than 1 car in the replay
                        # print(self.j)
                        self.j+=1

                        break

        if reverse and self.reverse_turn_activated: #### 3
            
            
            for i in range(len(self.saved_replay)):
                for j in range(len(self.saved_replay[i])):
                    # Starts with the first dictionary element in the snapshot list and iterates through  everything
                    x_pos = self.saved_replay[i][self.j]['position'][0]
                    y_pos = self.saved_replay[i][self.j]['position'][1]
                    angle = self.saved_replay[i][self.j]['angle']
                    
                    # Synchronises the current time with the replay time to display the replay in real time wuth a varience of ~0.04
                    if self.saved_replay[i][j]['time'] > self.timer and self.saved_replay[i][j]['time'] < self.timer+5:
                
                    
                        pos = pygame.Vector2(x_pos, y_pos)
                        self.replay_object.pos = pos

                        # Draws the hitbox around the replay cars
                        self.replay_object.update()
                        # pygame.draw .rect(GAME_DISPLAY, BLACK,
                        #                   self.replay_object.rect, 2)
                        self.replay_sprites_group.add(self.replay_object)

                        if self.replay_object.isCollided(self.car):
                            # Screen Shake animation to show collision
                            self.screen_shake = 10
                            self.collision()

                        # Blits the Car to the screen
                        rotated_image = pygame.transform.rotate(
                            self.replay_object.image, angle)
                        GAME_DISPLAY.blit(rotated_image, pos -
                                            (rotated_image.get_width() / 2, rotated_image.get_height() / 2))
                        # breaks out before it can blit more than 1 car in the replay
                        self.j -= 1

                        break

    def wallTeleport(self):
        # Places the user on the opposite side of the map when leaving to give them more options for routes

        # car_hitbox = (x, y, width, height)
        # Rectangular Based Collisions will be used for the cars as it resembles the shape nicely and is much
        #   faster than mask based collision (~ 112% Faster!) which adds up as more cars are added to the screen
        car_hitbox = self.car.rect
        # pygame.draw.rect(GAME_DISPLAY, BLACK, car_hitbox, 2)
        if car_hitbox[0] > DISPLAY_WIDTH:
            self.car.pos.x = 0
        if car_hitbox[0] + car_hitbox[2] < 0:
            self.car.pos.x = DISPLAY_WIDTH
        if car_hitbox[1] > DISPLAY_HEIGHT:
            self.car.pos.y = 0
        if car_hitbox[1] + car_hitbox[3] < 0:
            self.car.pos.y = DISPLAY_HEIGHT

    def powerUp(self, loc, powerup_choice):

        # Draws rectangle around every locations
        # for i in range(len(power_up_recs)):
        #     pygame.draw.rect(GAME_DISPLAY, RED, power_up_recs[i], 2)
        # Drwas rectangle around icon hitbox slo
        # pygame.draw.rect(GAME_DISPLAY, RED, power_up_recs[loc], 2)

        # [0] = heart
        # [1] = speedup
        # [2] = slowdown
        # [3] = shield
        # [4] = reverse
        # [5] = route

        # Only Blits the powerup if it hasn't been collected
        if not self.powerup_collided:
            GAME_DISPLAY.blit(
                list_of_powerups[powerup_choice], (power_up_recs[loc][0], power_up_recs[loc][1]))

        # Handles each power up after collision
        if self.car.rect.colliderect(power_up_recs[loc]):

            # Heart
            if powerup_choice == 0:
                self.powerup_collided = True
                self.health_collected = True

            # Speedup
            elif powerup_choice == 1:
                self.powerup_collided = True
                self.speedeup_collected = True

            # Slowdown
            elif powerup_choice == 2:
                self.powerup_collided = True
                self.slowdown_collected = True

            # Shield
            elif powerup_choice == 3:
                self.powerup_collided = True
                self.shield_collected = True

            # Reverse
            elif powerup_choice == 4:
                
                self.powerup_collided = True
                self.reverse_collected = True

            # Route
            elif powerup_choice == 5:
                self.powerup_collided = True
                self.route_collected = True

    def healthPowerUp(self):
        self.player_health = 200

    def speedupPowerUp(self):

        if self.powerup_timer < 3.6:
            displayMessage(
                f"Time: {int(self.powerup_timer)}", YELLOW, 35, (200, 10))
            self.car.max_vel = 25
            self.car.vel.x = 25

        dt = self.dt / 10
        self.powerup_timer -= dt

        if self.powerup_timer <= 0:
            if self.car_choice == 1:
                self.car.vel.x = 18
                self.car.max_vel = 18
                self.speedup_activated = False
            elif self.car_choice == 2:
                self.car.vel.x = 14
                self.car.max_vel = 14
                self.speedup_activated = False

    def slowdownPowerUp(self):
        if self.powerup_timer < 3.6:
            displayMessage(
                f"Time: {int(self.powerup_timer)}", YELLOW, 35, (200, 10))
            self.car.max_vel = 10
            self.car.vel.x = 10

        dt = self.dt / 10
        self.powerup_timer -= dt

        if self.powerup_timer <= 0:
            if self.car_choice == 1:
                self.car.vel.x = 18
                self.car.max_vel = 18
                self.slowdown_activated = False
            elif self.car_choice == 2:
                self.car.vel.x = 14
                self.car.max_vel = 14
                self.slowdown_activated = False

    def shieldPowerUp(self):

        if self.powerup_timer < 3.6:
            displayMessage(
                f"Time: {int(self.powerup_timer)}", YELLOW, 35, (200, 10))

            GAME_DISPLAY.blit(
                shield_image, (self.car.rect.x-20, self.car.rect.y-20))

        dt = self.dt / 10
        self.powerup_timer -= dt

        if self.powerup_timer <= 0:
            self.shield_activated = False

    def reversePowerUp(self):

        #Allows for control over the reverse replay
        self.reverse_turn_activated = True
        
        if self.powerup_timer < 3.6:
            displayMessage(
                f"Time: {int(self.powerup_timer)}", YELLOW, 35, (200, 10))
            
            self.replay_reverse = True

        dt = self.dt / 10
        self.powerup_timer -= dt

        if self.powerup_timer <= 0 or self.j <= 0:
            self.replay_reverse = False
            self.reverse_activated = False

    def routePowerUp(self):

        if self.powerup_timer < 3.6:
            displayMessage(
                f"Time: {int(self.powerup_timer)}", YELLOW, 35, (200, 10))

            for i in range(len(self.saved_replay)):
                for j in range(len(self.saved_replay[i])):

                    x_pos = self.saved_replay[i][j]['position'][0]
                    y_pos = self.saved_replay[i][j]['position'][1]
                    angle = self.saved_replay[i][j]['angle']

                    pos = pygame.Vector2(x_pos, y_pos)

                    rotated_image = pygame.transform.rotate(
                        show_route_image, angle)
                    GAME_DISPLAY.blit(rotated_image, pos -
                                      (rotated_image.get_width() / 2, rotated_image.get_height() / 2))

        dt = self.dt / 10
        self.powerup_timer -= dt

        if self.powerup_timer <= 0:
            self.route_actived = False

    def saveScore(self):
        # Saves the score/highscore to be read by game over menu

        # Save current score
        with open(path_2+'/currentscore.txt', 'w') as f:
            f.write(str(self.turn_count))

        # Checks to update highscore if needed
        try:
            with open(path_2+'/highscore.txt', 'r') as f:
                high_score = f.read()
                if self.turn_count > int(high_score):
                    with open(path_2+'/highscore.txt', 'w') as e:
                        e.write(str(self.turn_count))
        except ValueError:
            pass

    def collision(self):
        # Plays Shake Animation after Collision unless shield powerup is activated

        if self.shield_activated:
            # Ignore collisions if the shield is activated
            pass
        else:
            if self.screen_shake > 0:
                if self.shield_activated:
                    # Allows for shield powerup to be activated whilst taking damage
                    pass
                else:
                    self.scroll[0] += randint(0, 8) - 4
                    self.scroll[1] += randint(0, 8) - 4
                    crash_fx.set_volume(0.1)
                    crash_fx.play()
                    self.createMap(self.scroll[0], self.scroll[1])
                    self.createTimer()

                    # Reduces Health
                    if self.car_choice == 1:
                        self.car.health -= 30
                        self.player_health = self.car.health
                    elif self.car_choice == 2:
                        self.car.health -= 20
                        self.player_health = self.car.health

                    self.screen_shake -= 1

    def drawHealthBar(self):

        # Health Bar
        GAME_DISPLAY.blit(middle_rectangle_image, (0, 0))
        GAME_DISPLAY.blit(red_healthbar_image, (0, 0))
        for health in range(self.player_health):
            GAME_DISPLAY.blit(green_health_image, (health+459, 11))

    def showPowerUp(self):

        GAME_DISPLAY.blit(powerup_rectangle_image, (-70, 600))
        if self.health_collected:
            GAME_DISPLAY.blit(heart_powerup_image, (7, 620))
        elif self.speedeup_collected:
            GAME_DISPLAY.blit(speedup_powerup_image, (7, 620))
        elif self.slowdown_collected:
            GAME_DISPLAY.blit(slowdown_powerup_image, (7, 620))
        elif self.shield_collected:
            GAME_DISPLAY.blit(shield_powerup_image, (7, 620))
        elif self.reverse_collected:
            GAME_DISPLAY.blit(reverse_replay_powerup_image, (7, 620))
        elif self.route_collected:
            GAME_DISPLAY.blit(show_route_powerup_image, (7, 620))

    def events(self):
        # Handles quit event

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                # Makes them red to be easily seen over the pause menu screen
                displayMessage(f"Turn: {self.turn_count}", RED, 35, (24, 10))
                displayMessage(f"Time: {int(self.timer)}", RED, 35, (1100, 10))
                pauseMenu()
                self.update()  # Stops the car from having a mind of it's own due to things breaking when the clock is not being ticked

            #Car Control ------------------------------------------------------------------#
            # Encapsulates all the presses in a KEYDOWN event to
            # prevent game stutters not registering the key press and assigning a value of 0 by mistake
            if event.type == pygame.KEYDOWN:
                if key[pygame.K_a] or key[pygame.K_LEFT]:
                    self.car.turning += 20   # Positive Rotates Anti Clockwise
                if key[pygame.K_d] or key[pygame.K_RIGHT]:
                    self.car.turning -= 20  # Negative angles rotate Clockwise

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.car.turning = 0

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.car.turning = 0

    def update(self):
        pygame.display.update()
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    main_object = Main()

    pygame.display.quit()
    pygame.quit()
