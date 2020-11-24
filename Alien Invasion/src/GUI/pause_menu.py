import pygame
import sys
from GUI.button import Button

class PauseMenu:

    def __init__(self, width, height, screen):
        """Draws the pause menu and displays it on game play screen, which is passed in from alien_invasion.py"""

        self.__screen = screen
        
        # will be true when pause menu is active.
        self.__pauseMenuActive = False

        # will be used to see if user clicked 'Main Menu' button.
        self.__toMainMenu = False

        size = (width*0.18, height*0.42) # will be same postition no matter screen resolution.
        position = (width*0.41, height*0.30) # will allow menu to be centered, no matter the resolution.

         # create image
        self._image = pygame.Surface(size)

        # fill image with color - white
        self._image.fill((255,255,255))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # draws rectangle with to main menu button and other buttons

        # creates Pause title on menu.
        self.__pausedTitle = Button((width*0.45, height*0.32), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__pausedTitle.add_image("images\paused.png")

        # creates resume button
        self.__resumeButton = Button((width*0.45, height*0.4), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__resumeButton.add_image("images\\resume_button.png")

        # creates main menu button
        self.__mainMenuButton = Button((width*0.45, height*0.5), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__mainMenuButton.add_image("images\main_menu_button.png")

        # creates exit game button
        self.__exitGameButton = Button((width*0.45, height*0.6), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__exitGameButton.add_image("images\exit_game_button_pause_menu.png")

        


    def run_pause_menu(self):
        """Runs the pause menu, till user wants to exit it or the game."""

        self.__pauseMenuActive = True
        while self.__pauseMenuActive == True:
            # draw pause menu
            self.drawPauseMenu()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # watch for paused menu event
            self._check_for_events()



    def drawPauseMenu(self):
        """Draws the pause menu and puts it on the game play screen and returns it."""

        # draws pause menu
        self.__screen.blit(self._image, self._rect)

        # draws buttons
        self.drawButtons()


    def drawButtons(self):
        """Draws button for pause menu."""
        self.__pausedTitle.draw(self.__screen)
        self.__exitGameButton.draw(self.__screen)
        self.__resumeButton.draw(self.__screen)
        self.__mainMenuButton.draw(self.__screen)

    def _check_for_events(self):
        """Checks for events in pause menu."""

        for event in pygame.event.get():
            # if user exits out of window during pause menu
            if event.type == pygame.QUIT:
                sys.exit()

            # if user presses escape to unpause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__pauseMenuActive = False

            # if exit game button is pressed
            if self.__exitGameButton.isButton_pressed_event_handler(event) == True:
                sys.exit()

            # if resume button is pressed
            if self.__resumeButton.isButton_pressed_event_handler(event) == True:
                self.__pauseMenuActive = False

            # if main menu button is pressed
            if self.__mainMenuButton.isButton_pressed_event_handler(event) == True:
                self.__pauseMenuActive = False
                self.__toMainMenu = True


    def get_to_main_menu(self):
        """Returns value of toMainMenu."""
        return self.__toMainMenu



