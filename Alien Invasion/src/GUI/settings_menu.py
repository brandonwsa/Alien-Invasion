import pygame
from GUI.button import Button
from GUI.menu import Menu

class SettingsMenu(Menu):
    """Creates settings screen"""

    def __init__(self, width, height, screen, settings):
        """Extends menu.py __init__"""

        # initiates super __init__
        super().__init__(width, height, screen)

        # uses settings object created in alien_invasion.py
        self.__settings = settings

        # Create change screen resolution button
        self.__changeResButton = Button((width*0.45, height*0.6), (width/9.6, height/14.4))
        self.__changeResButton.add_image("images\change_resolution_button.png")
                    


    def _draw_buttons(self):
        """Extends _draw_buttons from menu.py and adds resolution button."""

        super()._draw_buttons()

        # draw change resolution button
        self.__changeResButton.draw(self._screen)



    def _check_for_events(self):
        """Overrides _check_for_events from menu.py and adds event for clicking resolution button."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if back button is pressed
            if self._backButton.isButton_pressed_event_handler(event) == True:
                self._showPreviousScreen = True # will exit the while loop and return back to Main Menu.

            # if change resolution is pressed
            if self.__changeResButton.isButton_pressed_event_handler(event) == True:
                self.changeScreenResolution() # will call method inside this object to change resolution.
                print(self.__settings.get_res_width())
                print(self.__settings.get_res_height())



    def changeScreenResolution(self):
        """Allows user to change the resolution. Calls settings methods. Needs more work done."""

        # prompts user for reolution from console
        try:
            new_width = int(input("Enter new resolution width: "))
            new_height = int(input("Enter new resolution height: "))
        except:
            print("Error collecting new resolution width and height from user. Res may not be an int.")

        # display resolutions in console for confirmation
        print(f"width = {new_width}, height = {new_height}")

        # calls set resolution methods from settings object
        self.__settings.set_res_width(new_width)
        self.__settings.set_res_height(new_height)
        self.__screen = pygame.display.set_mode((self.__settings.get_res_width(), self.__settings.get_res_height())) # may need to work with only one screen object for every menu and display.

        