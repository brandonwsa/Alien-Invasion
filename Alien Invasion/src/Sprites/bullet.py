import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired form the ship."""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.__screen = screen
        self.__ship = ship

        # bullet settings | may need to add to settings.py if each bullet makes a new bullet object. This will save memory by making less variables.
        self.__speed = 10.0
        self.__width = 3
        self.__height = 15
        self.__color = (60, 60, 60)

        # create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.rect.midtop = self.__ship.getRect().midtop

        # get bullet start position (AKA ships midtop position)
        self.__ship_x = self.rect.midtop[0]
        self.__ship_y = self.rect.midtop[1]

        # get mouse position of X and Y
        self.__cursor_pos = pygame.mouse.get_pos()
        self.__cursor_x = self.__cursor_pos[0]
        self.__cursor_y = self.__cursor_pos[1]

        # bullets x and y bullet velocity, set to 1 by default.
        self.__x_velocity = 1.0
        self.__y_velocity = 1.0

        # store the bullet's position as a decimal vlaue.
        self.__y = float(self.rect.y)
        self.__x = float(self.rect.x)



    def update(self):
        """Move the bullet on the screen."""

        # calculate bullet velocity(movement) from ship to cursor position, where aimed at
        self._calc_bullet_velocity()

        # update the decimal position of the bullet. | maybe add the additional feature of adding __speed ontop of velocity too.
        if self.__ship_x < self.__cursor_x: # if ship is to the left of cursor on the screen
            self.__x += self.__x_velocity * self.__speed  
        elif self.__ship_x > self.__cursor_x: # if ship is to the right of cursor on the screen
            self.__x -= self.__x_velocity * self.__speed

        if self.__ship_y < self.__cursor_y: # if ship is above cursor on the screen
            self.__y += self.__y_velocity * self.__speed
        else:
            self.__y -= self.__y_velocity * self.__speed

        # update the rect position.
        self.rect.y = self.__y
        self.rect.x = self.__x



    def _calc_bullet_velocity(self):
        """Calculates bullet movement by using ship positin when fired and cursor position."""
        # find difference between ship and cursor positions. Will work with only positives and reinforces to work only with positive ints.
        if self.__ship_x > self.__cursor_x:
            x_diff = self.__ship_x - self.__cursor_x
        else:
            x_diff = self.__cursor_x - self.__ship_x
        
        if self.__ship_y > self.__cursor_y:
            y_diff = self.__ship_y - self.__cursor_y
        else:
            y_diff = self.__cursor_y - self.__ship_y

        # find velocity for X in which Y is moved by 1 pixel
        self.__x_velocity = x_diff / y_diff




    def draw_bullet(self):
        """Draws the bullet to the screen."""
        pygame.draw.rect(self.__screen, self.__color, self.rect)


    def getRect(self):
        """Gets the rect of bullet."""
        return self.rect
    