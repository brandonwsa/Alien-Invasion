import pygame
from random import randint
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clas to manage Aliens."""

    def __init__(self, screen, speed):
        """Initializes the Alien and sets its starting location."""

        super().__init__()

        self.__screen = screen

        # load the alien image and get its rect.
        self.image = pygame.image.load('images\green_alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien at a random X coordinate
        self.rect.x = self.rect.width #randint(100, 1820)
        self.rect.y = self.rect.height
       # self.rect.midbottom = self.__screen_rect.midbottom

        # store alien's exact horizontal and vertical positions
        self.__x = float(self.rect.x)
        self.__y = float(self.rect.y)

        # alien speed
        self.__speed = speed

        # drop speed
        self.__drop_speed = 10


    def check_edges(self):
      """Return True if alien is at edge of screen."""
      self.__screen_rect = self.__screen.get_rect()

      if self.rect.right >= self.__screen_rect.right or self.rect.left <= 0:
        return True



    def update(self, fleet_direction):
      """Move the alien to the right or left."""
      # multiplies speed by either 1 or -1, depending on fleet direction. Check settings.py for details.
      self.__x += (self.__speed * fleet_direction) # takes fleet direction, passed from alieninvasion.py from settings.py
      self.rect.x = self.__x



    def getWidth(self):
      """Return the alien width size."""
      return self.rect.width

    def getHeight(self):
      """Return the alien height size."""
      return self.rect.height


    def setX(self, x):
      """Sets a new X value for alien."""
      self.__x = x


    def getX(self):
      """Returns alien's x value."""
      return self.__x


    def getDropSpeed(self):
      """Returns drop speed of alien."""
      return self.__drop_speed

