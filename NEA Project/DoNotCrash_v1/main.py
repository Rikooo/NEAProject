import pygame
import json
from os import path, getcwd
from button import *
from misc import *

pygame.init()

# Game Window --------------------------------------------------------------------------#
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
GAME_DISPLAY = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT))


def displayMessage(text, text_colour, text_size, coords):
    font = pygame.font.Font(
        'NEA Project\external files\street.ttf', text_size)
    textSurface = font.render(text, False, text_colour)
    GAME_DISPLAY.blit(textSurface, coords)


# Menu Systems ----------------------------------------------------------------------------#
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handles what to do after the user clicks on the corresponding button
                if play_game_button.mouseOver(pos):
                    running = False
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

    def __init__(self):
        # Initialisations ----------------------------------------------------------------------#
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Game Window --------------------------------------------------------------------------#
        pygame.display.set_caption('Do Not Crash!')
        pygame.display.set_icon(game_icon_image)

        # Runs Main Method ---------------------------------------------------------------------#
        self.running = True
        self.initial_run = True
        self.run()

    def run(self):
        # Main game loop
        while self.running:
            if self.initial_run:
                mainMenu()
                self.initial_run = False

            # Placeholder as map is not created yet
            GAME_DISPLAY.fill((0, 0, 90))
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.events()

    def events(self):
        # Handles quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseMenu()


# Calls main when the program runs
if __name__ == "__main__":
    main_object = Main()

    # If all else fails, call back to quit
    pygame.display.quit()
    pygame.quit()
