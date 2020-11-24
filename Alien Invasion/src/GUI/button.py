import pygame

class Button:

    def __init__(self, position, size):
        """Initialized button object, making a default image color and getting the size of the button"""

        # create image
        self._image = pygame.Surface(size)

        # fill image with color - red
        self._image.fill((255,0,0))

        # get image size and position
        self._rect = pygame.Rect(position, size)
        

    def draw(self, screen):

        # draw selected image
        screen.blit(self._image, self._rect)

    def isButton_pressed_event_handler(self, event):
        """Call with an event when checking if the button was pressed
            returns true if button was pressed."""

        # Checks if the button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    return True

    def add_image(self, imagePath):
        """Allows a button to have an image, just supply the image path when calling this method."""

        # loads image.
        buttonImage = pygame.image.load(imagePath)

        # puts image on button.
        self._image.blit(buttonImage, (0, 0)) 