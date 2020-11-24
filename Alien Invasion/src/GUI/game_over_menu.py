import pygame
import sys
from GUI.button import Button

class GameOverMenu:

    def __init__(self, width, height, screen):
        """Draws the game over menu and displays it on game play screen, which is passed in from alien_invasion.py"""

        self.__screen = screen
        
        # will be true when game over menu is active.
        self.__gameOverMenuActive = False

        # will be used to see if user clicked 'Main Menu' button.
        self.__toMainMenu = False

        # will be used ot see if user clicked 'Play Again' button.
        self.__play_again = False

        size = (width*0.18, height*0.42) # will be same postition no matter screen resolution.
        position = (width*0.41, height*0.30) # will allow menu to be centered, no matter the resolution.

         # create image
        self._image = pygame.Surface(size)

        # fill image with color - white
        self._image.fill((255,255,255))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # draws rectangle with to main menu button and other buttons

        # creates game over title
        self.__gameOverTitle = Button((width*0.45, height*0.32), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__gameOverTitle.add_image("images\game_over.png")

        # creates playAgain button
        self.__playAgainButton = Button((width*0.45, height*0.4), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__playAgainButton.add_image("images\play_again_button.png")

        # creates main menu button
        self.__mainMenuButton = Button((width*0.45, height*0.5), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__mainMenuButton.add_image("images\main_menu_button.png")

        # creates exit game button
        self.__exitGameButton = Button((width*0.45, height*0.6), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__exitGameButton.add_image("images\exit_game_button_pause_menu.png")

        


    def run_game_over_menu(self):
        """Runs the game over menu, till user wants to exit it or the game."""

        self.__gameOverMenuActive = True
        while self.__gameOverMenuActive == True:
            # draw game over menu
            self.drawGameOverMenu()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # watch for paused menu event
            self._check_for_events()



    def drawGameOverMenu(self):
        """Draws the game over menu and puts it on the game play screen and returns it."""

        # draws game over menu
        self.__screen.blit(self._image, self._rect)

        # draws buttons
        self.drawButtons()


    def drawButtons(self):
        """Draws button for game over menu."""
        self.__gameOverTitle.draw(self.__screen)
        self.__exitGameButton.draw(self.__screen)
        self.__playAgainButton.draw(self.__screen)
        self.__mainMenuButton.draw(self.__screen)

    def _check_for_events(self):
        """Checks for events in game over menu."""

        for event in pygame.event.get():
            # if user exits out of window during game over menu
            if event.type == pygame.QUIT:
                sys.exit()

            # if user presses escape to unpause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__gameOverMenuActive = False

            # if exit game button is pressed
            if self.__exitGameButton.isButton_pressed_event_handler(event) == True:
                sys.exit()

            # if playAgain button is pressed
            if self.__playAgainButton.isButton_pressed_event_handler(event) == True:
                self.__gameOverMenuActive = False
                self.__play_again = True

            # if main menu button is pressed
            if self.__mainMenuButton.isButton_pressed_event_handler(event) == True:
                self.__gameOverMenuActive = False
                self.__toMainMenu = True


    def get_to_main_menu(self):
        """Returns value of toMainMenu."""
        return self.__toMainMenu

    def play_again(self):
        """Returns boolean value of play again."""
        return self.__play_again



