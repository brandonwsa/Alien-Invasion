import pygame.font

class GameStats:
    """Track stats for alien invasion."""

    def __init__(self, ship_limit):
        """Initializes stats."""
        # how many lives player starts with
        self.__ship_limit = ship_limit

        # starts alien invasion in an active state.
        self.__game_active = True # will be false when player runs out of lives.

        self.reset_stats()


    def reset_stats(self):
        """Initializes stats that can change during the game."""
        self.__ships_left = self.__ship_limit
        self.__game_active = True
        self.__score = 0 # used to keep score. Will reset when player dies, etc.


    def initialize_bullet_display(self, screen, bullets, bgColor):
        """Initializes what is need to display bullets to screen."""
        self.__screen = screen
        self.__screen_rect = self.__screen.get_rect()
        self.__remaining_bullets = bullets
        self.__bgColor = bgColor # background color of gameplayscreen

        # font settings for scoring information.
        self.__text_color = (100, 100, 100)
        self.__font = pygame.font.SysFont(None, 48)

        # prepare intialize bullet display.
        self.prep_bullets_display(self.__remaining_bullets)


    # setters
    def set_ships_left(self, remaining_ships):
        """Set ships left."""
        self.__ships_left = remaining_ships


    # getters
    def get_ships_left(self):
        """Returns number of ship loves left."""
        return self.__ships_left


    def get_game_active_state(self):
        """Returns boolean value of game state, based on player lives."""
        return self.__game_active

    def get_score(self):
        """Returns value of score."""
        return self.__score




    def has_more_lives(self, more_lives):
        """Sets the activity of the game. False if player has no more lives, True if has more lives."""
        self.__game_active = more_lives

    def increase_score(self, points):
        """Increases the score."""
        self.__score += points


    def prep_bullets_display(self, bullets):
        """turn bullets remaining into rendered image"""
        # get bullets in string form after formatting with commas
        bullets_str = "{:,}".format(bullets)
        # render string as image with text color and bg color
        self.__bullets_image = self.__font.render(bullets_str, True, self.__text_color, self.__bgColor)

        # display the bullets at the bottom right of the screen.
        self.__bullets_rect = self.__bullets_image.get_rect()
        self.__bullets_rect.right = self.__screen_rect.right - 20 # offset bullets to 20 pixels left of right side of screen.
        self.__bullets_rect.bottom = self.__screen_rect.bottom - 20 # will be displayed 20 pixels from bottom of screen


    def show_bullets_remaining(self):
        """Draws total bullet remaining to screen."""
        self.__screen.blit(self.__bullets_image, self.__bullets_rect)
