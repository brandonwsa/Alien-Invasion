import pygame
from GUI.button import Button
from GUI.menu import Menu

class ScoreboardMenu(Menu):
    """Creates Scoreboard screen"""

    def __init__(self, width, height, screen):
        """Makes display window for Scoreboard, using menu.py as super"""

        super().__init__(width, height, screen)
    