import pygame
# import sys

class GamePlayScreen:
    """Creates the game play screen"""

    def __init__(self, screen):

        self.__screen = screen

        # make background color
        self.__bgColor = (0, 0, 0)


    def getScreen(self):
        return self.__screen

    def get_bg_color(self):
        """Returns back ground color."""
        return self.__bgColor

    def drawScreen(self):
        """Will draw game play screen."""

        self.__screen.fill(self.__bgColor)