import pygame
import json
import os

from button import *
from misc import *
from testcar import *

pygame.init()

# Game Window ----------------------------------------------------------------------------#
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
GAME_DISPLAY = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT))


path = os.path.dirname(os.path.dirname(__file__))


def displayMessage(text, text_colour, text_size, coords):
    font = pygame.font.Font(
        path+'/External Files/street.ttf', text_size)
    textSurface = font.render(text, False, text_colour)
    GAME_DISPLAY.blit(textSurface, coords)


# # Menu Systems ----------------------------------------------------------------------------#
def mainMenu():
    # Individual Menu Buttons                   #Size   x   y  width height
    play_game_button = Button("PLAY GAME", ORANGE, 90, 50, 100, 460, 75)
    choose_car_button = Button("CHOOSE CAR", ORANGE, 75, 80, 220, 400, 65)
    options_button = Button("OPTIONS", ORANGE, 75, 80, 330, 280, 65)
    quit_button = Button("QUIT", ORANGE, 75, 80, 440, 160, 65)

    running = True
    while running:
        # Displays Background Image First
        GAME_DISPLAY.blit(main_menu_image, (0, 0))
        # Draws Each button to the screen
        play_game_button.draw(GAME_DISPLAY)
        choose_car_button.draw(GAME_DISPLAY)
        options_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handles what to do after the user clicks on the corresponding button
                if play_game_button.mouseOver(pos):
                    # This avoids the current state of whatever menu system overriding the intended menu
                    # For example before this, when the user would pause the game and exit to main menu then click play game,
                    # They would immidiately arrive at the pause screen an not the actual game hence the use of a default parameter
                    Main(initial_run=False)
                elif choose_car_button.mouseOver(pos):
                    chooseCarMenu()
                elif options_button.mouseOver(pos):
                    pass
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

        pygame.display.update()


def chooseCarMenu():
    # Individual Menu Buttons               #Size  x   y  width height
    play_button = Button("Play", NEON_GREEN, 60, 1100, 520, 160, 75)
    main_menu_button = Button("Main Menu", NEON_GREEN, 60, 20, 520, 330, 75)
    quit_button = Button("Quit", NEON_GREEN, 60, 1100, 0, 160, 75)

    running = True
    while running:
        # Displays Background Image First
        GAME_DISPLAY.blit(choosing_menu_image, (0, 0))
        # Draws Each button to the screen
        play_button.draw(GAME_DISPLAY)
        main_menu_button.draw(GAME_DISPLAY)
        quit_button.draw(GAME_DISPLAY)
        GAME_DISPLAY.blit(arrow_left_image, (25, 620))
        GAME_DISPLAY.blit(arrow_right_image, (1150, 620))
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
                else:
                    play_button.text_colour, play_button.text_size = NEON_GREEN, 60
                    main_menu_button.text_colour, main_menu_button.text_size = NEON_GREEN, 60
                    quit_button.text_colour, quit_button.text_size = NEON_GREEN, 60

            # HANDLING --------------------------------------------------------------------#
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handles what to do after the user clicks on the corresponding button
                if play_button.mouseOver(pos):
                    pass
                elif main_menu_button.mouseOver(pos):
                    mainMenu()
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

        pygame.display.update()


def optionMenu():
    pass


def pauseMenu():
    # Individual Menu Buttons                 #Size   x   y  width height
    resume_button = Button("Resume Game", ORANGE, 90, 365, 200, 545, 75)
    # Placed Button Left Area
    main_menu_button = Button("Main Menu",
                              ORANGE, 60, 20, 520, 330, 75)
    quit_button = Button("Quit Game", ORANGE, 90, 415, 310, 445, 75)

    running = True
    while running:
        GAME_DISPLAY.fill((0, 0, 90))
        # Paused message doesn't need to be a button hence the use of displayMessage()
        displayMessage("- PAUSED - ", WHITE, 80, (475, 50))
        # No need to fill background as pause menu should be placed 'above' the gmae window so user can see their progress
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handles what to do after the user clicks on the corresponding button
                if resume_button.mouseOver(pos):
                    # Returns the user back to the game
                    running = False  # Breaks out of while loop
                    return True  # Breaks out of function
                elif main_menu_button.mouseOver(pos):
                    mainMenu()
                elif quit_button.mouseOver(pos):
                    pygame.display.quit()
                    pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Adds a little convinience so if the user wants to return to the game without having to click any buttons they can do so
                if event.key == pygame.K_ESCAPE:
                    running = False  # Breaks out of while loop
                    return True  # Breaks out of function
        pygame.display.update()


class Main:
    """ Class controls the entire program """

    def __init__(self, initial_run=True):
        # Initialisations ----------------------------------------------------------------------#
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Game Window --------------------------------------------------------------------------#
        pygame.display.set_caption('Do Not Crash!')
        pygame.display.set_icon(game_icon_image)

        # Runs Main Methods --------------------------------------------------------------------#
        self.running = True
        self.initial_run = initial_run
        self.run()

    def run(self, running=False):
        # Main game loop
        test_car = Test_Car(0, 0)  # Places car initially at (0,0)

        while self.running:
            if self.initial_run:
                mainMenu()  # The function makes initial run = False otherwise the saved state will carry on between menu screens

            # TEMP PLACEHOLDER #

            # # Time in ms since the last update aka Change in time
            # dt = self.clock.get_time() / 1000
            # print("Previous dt: ", dt)
            # test_car.getEverything()

            # TEMP PLACEHOLDER #

            self.createMap(test_car)
            self.handleCar(test_car)
            self.events()
            self.update()

    def createMap(self, test_car):
        # Handles all objects seen on the map
        GAME_DISPLAY.fill((0, 0, 90))
        GAME_DISPLAY.blit(car_sprite, test_car.getPosition())

    def handleCar(self, test_car):
        # Handles the car logic
        # Time in ms since the last update aka Change in time
        dt = self.clock.get_time() / 1000
        test_car.accelerate(dt)
        # print(test_car.getPosition())
        displayMessage(
            f"Current Vel: {test_car.vel}", WHITE, 30, (500, 500))

    def events(self):
        # Handles quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pauseMenu()

            # Car Control ------------------------------------------------------------------#
            if key[pygame.K_a]:
                pass
            if key[pygame.K_d]:
                pass

    def update(self):
        pygame.display.update()
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    main_object = Main()

    pygame.display.quit()
    pygame.quit()
