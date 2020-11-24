import pygame

class Ship:
    """Class to manage ship"""

    def __init__(self, screen): # may need to pass alieninvasion object instead
        """Initialize the ship and set its starting position."""

        self.__screen = screen
        self.__screen_rect = screen.get_rect()

        # load the ship image and get its rect.
        self.__image = pygame.image.load('images\ship.bmp')
        self.rect = self.__image.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.__screen_rect.midbottom

        # movement flag
        self.__moving_right = False
        self.__moving_left = False
        self.__moving_up = False
        self.__moving_down = False

        # ship movement velocity
        self.__velocity = 1


    def blitme(self):
        """Draw ship at its current location."""
        self.__screen.blit(self.__image, self.rect)



    def update(self):
        """Update the ship's position based on the movement flag."""

        # if moving right and ships position is less than max X value of screen
        if self.__moving_right and self.rect.right < self.__screen_rect.right:
            self.rect.x += self.__velocity # move image right one pixel

        # if moving left and ships position is more than min X value of screen
        if self.__moving_left and self.rect.left > 0:
            self.rect.x -= self.__velocity # move image left one pixel

        # if moving up and ships position is below the top half of the screen
        if self.__moving_up and self.rect.top > self.__screen_rect.height/2:
            self.rect.y -= self.__velocity # move image up one pixel

        # if moving down and ships position is above bottom of the screen
        if self.__moving_down and self.rect.bottom < self.__screen_rect.height:
            self.rect.y += self.__velocity # move image down one pixel



    def center_ship(self):
        """Re centers the ship on the screen. Used if ship is destroyed by alien."""
        self.rect.midbottom = self.__screen_rect.midbottom



    def setMovingRight(self, value):
        """Sets __moving_right to true or false."""
        self.__moving_right = value


    def setMovingLeft(self, value):
        """Sets __moving_left to true or false."""
        self.__moving_left = value


    def setMovingUp(self, value):
        """Sets __moving_up to true or false."""
        self.__moving_up = value


    def setMovingDown(self, value):
        """Sets __moving_down to true or false."""
        self.__moving_down = value


    def setVelocity(self, value):
        """Sets __velocity to either 1 or 2."""
        self.__velocity = value

    def getRect(self):
        """Gets the ships rect."""
        return self.rect