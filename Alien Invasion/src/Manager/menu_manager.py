from GUI.main_menu import MainMenu
from GUI.instructions_menu import InstructionsMenu
from GUI.settings_menu import SettingsMenu
from GUI.scoreboard_menu import ScoreboardMenu
from GUI.pause_menu import PauseMenu
from GUI.game_over_menu import GameOverMenu
#from GUI.scoreboard import Scoreboard
#from GUI.settings_menu import SettingsMenu
#from instructions import Instructions

class MenuManager:
    """A Menu Manager to controll the display of the available menus, mainMenu, Scoreboard, settingsMenu, and instructions"""

    def __init__(self, settings, screen):
        """Takes in a Settings object to be used for window settings of each display, user defined and changeable in game
            Takes in screen object to be passed to each menu"""
        self.__settings = settings
        self.__screen = screen

        self.__toPlayScreen = False

        # userd to identify if user is trying to go back to main menu from gameplayscreen from pause menu.
        self.__goToMainMenu = False

        # used to identify is user is trying to play the game again from game over menu.
        self.__play_again = False

    def displayMainMenu(self):
        """Creates main menu object and displays main menu"""

        # Make Main Menu object and run it. Passes settings width and height, screen object and the menuManager object
        MM = MainMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen, self)
        MM.run_main_menu()

        # captures boolean value so alien_invasion.py can check to make sure user clicked a button to proceed.
        self.__toPlayScreen = MM.getToPlayScreen() # could potentially get rid of this method in main_menu.py and just have run_main_menu() return true once user clicks play. Will save code

        # garbage collects object when done in main menu.
        del MM 


    def displayInstructionsMenu(self):
        """Creates instructions menu object and displays it"""

        # Make instructions menu object
        IM = InstructionsMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen)
        IM.run_menu()

    def displaySettingsMenu(self):
        """Creates settings menu object and displays it"""

        # Make settings menu object. Passes settings object to be used for changing settings
        SM = SettingsMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen, self.__settings)
        SM.run_menu()

    def displayScoreboardMenu(self):
        """Creates settings menu object and displays it"""

        # Make settings menu object
        SBM = ScoreboardMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen)
        SBM.run_menu()


    def displayPauseMenu(self):
        """Creates pause menu object and displays it."""

        # make pause menu object
        PM = PauseMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen)
        PM.run_pause_menu()

        # checks if user clicked 'Main Menu' button
        if PM.get_to_main_menu() == True:
            self.__goToMainMenu = True
        else:
            self.__goToMainMenu = False


    def displayGameOverMenu(self):
        """Creates game over menu and displays it."""

        # make game over menu object.
        GOM = GameOverMenu(self.__settings.get_res_width(), self.__settings.get_res_height(), self.__screen)
        GOM.run_game_over_menu()

        # checks if user clicked 'Main Menu' button.
        if GOM.get_to_main_menu() == True:
            self.__goToMainMenu = True
        else:
            self.__goToMainMenu = False

        # checks if user clicked 'Play Again' button.
        if GOM.play_again(): # if true
            self.__play_again = True
        else:
            self.__play_again = False


    def goToPlayScreen(self):
        """Returns bool value of whether or not play screen should be displayed. If user pressed 'Play' bool value will be true"""
        return self.__toPlayScreen

    
    def get_go_to_main_menu(self):
        """Returns boolean value of if player is attempting to main menu from pause menu."""
        return self.__goToMainMenu


    def playAgain(self):
        """Returns boolean value of if player is attempting to play the game again from game over menu."""
        return self.__play_again
