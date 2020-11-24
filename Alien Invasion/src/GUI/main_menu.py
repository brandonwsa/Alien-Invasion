import sys
import pygame
#from alien_invasion import AlienInvasion
from settings import Settings
from GUI.button import Button
# from Manager.menu_manager import MenuManager

#was able to get alien invasion __screen to be called from here, not sure if refreshing __screen will work though.
#maybe there is a way to refresha picture or frame (fill) without changing previously made __screen until wanted to?
#Controller class?
#should the controller class call the menus and screens and handle the refilling? or should the menu and __screen classes handle that?

class MainMenu:
    """Draws Main Menu and keeps user here until changing to a different window
        Will call Menu Manager display methods to display settings menu, instrucitons menu, and scoreboard menu.
        Once user clicks 'Back' button in these menus, they will resume here in the Main Menu."""

    def __init__(self, width, height, screen, menuManager):
        """Initializes main menu __screen elements"""

        pygame.init()

        # initialize objects
        self.__screen = screen
        self.__menuManag = menuManager

        # when user clicks a button, turns to True to switch to play screen
        self.__toPlayScreen = False 

        # load the background image
        self.__bg = pygame.image.load("images\main_menu_background.png")

        # create main menu buttons
        # play button
        self.__playButton = Button((width*0.45, height*0.4), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__playButton.add_image("images\play_button.png")

        # instructions button
        self.__instructionsButton = Button((width*0.45, height*0.5), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__instructionsButton.add_image("images\instructions_button.png")

        # scoreboard button
        self.__scoreboardButton = Button((width*0.45, height*0.6), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__scoreboardButton.add_image("images\scoreboard_button.png")

        # settings button
        self.__settingsButton = Button((width*0.45, height*0.7), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__settingsButton.add_image("images\settings_button.png")

        # exit game button
        self.__exitGameButton = Button((width*0.45, height*0.8), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self.__exitGameButton.add_image("images\exit_game_button.png")



    def run_main_menu(self): 
        """Start the main loop for main menu __screen."""

        # stays in while loop till user clicks play
        while self.__toPlayScreen == False:

            #redraw the __screen during each pass through the loop
            # draws background image
            self.draw_background()

            # draws buttons
            self.draw_buttons()
 
            # Make the most recently drawn __screen visible.
            pygame.display.flip()

            # Watch for keyboard and mouse events.
            self._check_for_events()

            

    def draw_buttons(self):
        """Draws the main menu buttons"""

        self.__playButton.draw(self.__screen)
        self.__instructionsButton.draw(self.__screen)
        self.__scoreboardButton.draw(self.__screen)
        self.__settingsButton.draw(self.__screen)
        self.__exitGameButton.draw(self.__screen)



    def draw_background(self):
        """Draws the background image"""
        self.__screen.blit(self.__bg, (0, 0))



    def getToPlayScreen(self):
        """Returns toPlayScreen value for confirmation user actually pressed the button.
           Prevents the game from 'accidently' proceeding to game play __screen if user
           has not actually clicked the Play button. Called in menu_manager.py and value
           is used in alien_invasion.py"""
        return self.__toPlayScreen



    def _check_for_events(self):
        """Checks for events from user"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if play button is pressed
            if self.__playButton.isButton_pressed_event_handler(event) == True:
                self.__toPlayScreen = True # Exits loop

            # if instructions button is pressed
            if self.__instructionsButton.isButton_pressed_event_handler(event) == True:
                self.__menuManag.displayInstructionsMenu()

            # if settings button is pressed
            if self.__settingsButton.isButton_pressed_event_handler(event) == True:
                self.__menuManag.displaySettingsMenu()

            # if scoreboard button is pressed
            if self.__scoreboardButton.isButton_pressed_event_handler(event) == True:
                self.__menuManag.displayScoreboardMenu()

            # if exit game button is pressed
            if self.__exitGameButton.isButton_pressed_event_handler(event) == True:
                sys.exit()
