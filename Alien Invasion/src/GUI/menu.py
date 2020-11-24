import pygame
from GUI.button import Button

class Menu:
    """Is the deafult layout to be used for menus. Includes a back button and background image."""

    def __init__(self, width, height, screen):
        """Makes display window for menus"""

        self._screen = screen

        # if user clicks back, will be true
        self._showPreviousScreen = False

        # make background color
        self._bgColor = (0, 0, 0)

        # Create back button
        self._backButton = Button((width*0.45, height*0.4), (width/9.6, height/14.4)) # width/9.6 in 1920 = 200, height/14.4 in 1080p = 75
        self._backButton.add_image("images\\back_button.png")



    def run_menu(self):
        """Runs menu screen"""

        while self._showPreviousScreen == False: # will be true when user clicks back

            # Draws background
            self._draw_background()

            # Draw buttons
            self._draw_buttons()

            # Make the most recently drawn __screen visible.
            pygame.display.flip()

            # Watch for keyboard and mouse events.
            self._check_for_events()


    def _draw_buttons(self):
        """Draws buttons for menu screen"""

        self._backButton.draw(self._screen)



    def _draw_background(self):
        """Draws menu screen background"""

        self._screen.fill(self._bgColor)



    def _check_for_events(self):
        """Checks for events from user"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if back button is pressed
            if self._backButton.isButton_pressed_event_handler(event) == True:
                self._showPreviousScreen = True # will exit the while loop and return back to Main Menu.


        