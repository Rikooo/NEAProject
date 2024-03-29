import pygame
import json
import os

from button import *
from recources import *
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
        # Slightly above 10 to allow the user to react to the timer before counting down
        self.timer = 10.9
        self.turn_count = 0
        self.dt = 0  # (Explained bellow when value is assigned to it)

        # Game Window --------------------------------------------------------------------------#
        pygame.display.set_caption('Do Not Crash!')
        pygame.display.set_icon(game_icon_image)

        # Creates Object -----------------------------------------------------------------------#
        self.test_car = Test_Car(600, 600)  # Places car initially at (0,0)

        # Runs Main Methods --------------------------------------------------------------------#
        self.running = True
        self.initial_run = initial_run
        self.run()

    def run(self, running=False):
        # Main game loop

        while self.running:
            if self.initial_run:
                mainMenu()  # The function makes initial run = False otherwise the saved state will carry on between menu screens

            # This allows us to do integration for some physics simulation
            self.dt = self.clock.get_time() / 100
            self.createMap()
            self.createTimer()
            self.handleCar()
            self.events()
            self.update()

    def createMap(self):
        # Handles all objects seen on the map

        GAME_DISPLAY.fill((0, 0, 90))
        displayMessage(f"FPS: {self.clock.get_fps()}",
                       WHITE, 20, (1000, 400))
        rotated_image = pygame.transform.rotate(
            car_sprite, self.test_car.angle)

        GAME_DISPLAY.blit(rotated_image, self.test_car.pos -
                          (rotated_image.get_width() / 2, rotated_image.get_height() / 2))

    def createTimer(self):
        # Timer

        if self.timer < 10.9 and self.timer > 6:
            displayMessage(f"Time: {int(self.timer)}", WHITE, 35, (1100, 30))
        # Turns red when the clock hits 5 seconds to notify the user their turn is nearly over
        elif self.timer <= 6 and self.timer >= 4:
            displayMessage(f"Time: {int(self.timer)}", RED, 35, (1100, 30))
        # Shows ms for the last 3 seconds
        elif self.timer <= 4 and self.timer >= -1.1:  # -1.1 So the timer visual doesn't stop at 0.05 or similar
            displayMessage(
                f"Time: {self.timer:.2f}", RED, 35, (1100, 30))  # 2 decimal places

        dt = self.dt / 10  # Get's My Time in seconds
        self.timer -= dt

        if self.timer < 0:
            self.timer = 10  # Resets timer
            # Placeholder
            pauseMenu()  # This will pause the game, save the cars 'run' and accesses method to place car in a random position

    def handleCar(self):
        # Handles the car logic

        self.test_car.accelerate(self.dt)
        self.test_car.steering(car_sprite, self.dt)

        # Testing -------------------------------------------------------------------------#
        displayMessage(
            f"Current Turning: {self.test_car.turning}", WHITE, 20, (1000, 450))
        displayMessage(
            f"Current Vel: {self.test_car.vel}", WHITE, 20, (1000, 500))
        displayMessage(
            f"Current Accel: {self.test_car.accel}", WHITE, 20, (1000, 600))
        displayMessage(
            f"Current Angle: {self.test_car.angle}", WHITE, 20, (1000, 550))

    def events(self):
        # Handles quit event

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pauseMenu()
                self.update()  # Stops the car from having a mind of it's own due to things breaking when the clock is not being ticked

            #Car Control ------------------------------------------------------------------#
            # Encapsulates all the presses in a KEYDOWN event to
            # prevent game stutters not registering the key press and assigning a value of 0 by mistake
            if event.type == pygame.KEYDOWN:
                if key[pygame.K_a] or key[pygame.K_LEFT]:
                    self.test_car.turning += 20   # Positive Rotates Anti Clockwise
                if key[pygame.K_d] or key[pygame.K_RIGHT]:
                    self.test_car.turning -= 20  # Negative angles rotate Clockwise

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.test_car.turning = 0

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.test_car.turning = 0

    def update(self):
        pygame.display.update()
        self.clock.tick(self.FPS)


if __name__ == "__main__":
    main_object = Main()

    pygame.display.quit()
    pygame.quit()
