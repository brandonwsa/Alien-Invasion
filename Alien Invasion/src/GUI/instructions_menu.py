import pygame
from GUI.button import Button
from GUI.menu import Menu

class InstructionsMenu(Menu):
    """Creates instructions screen, using menu.py as super"""

    def __init__(self, width, height, screen):
        """Makes display window for instructions, using menu.py as super"""

        super().__init__(width, height, screen)

