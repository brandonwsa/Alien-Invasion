import pygame.font

class Scoreboard:
    """Class to keep track of and report player score."""

    def __init__(self, screen, score, bgColor):
        """Initialize scorekeeping attributes."""
        self.__screen = screen
        self.__screen_rect = self.__screen.get_rect()
        self.__score = score
        self.__bgColor = bgColor # background color of gameplayscreen

        # font settings for scoring information.
        self.__text_color = (100, 100, 100)
        self.__font = pygame.font.SysFont(None, 48)

        # prepare the initial score image.
        self.prep_score(score)


    def prep_score(self, score):
        """Turn the score into a rendered image."""
        # get score in string form after formatting with commas
        score_str = "{:,}".format(score)
        # render string as image with text color and bg color
        self.__score_image = self.__font.render(score_str, True, self.__text_color, self.__bgColor)

        # display the score at the top right of the screen.
        self.__score_rect = self.__score_image.get_rect()
        self.__score_rect.right = self.__screen_rect.right - 20 # offset score to 20 pixels left of right side of screen.
        self.__score_rect.top = 20 # will be displayed 20 pixels from top of screen



    def show_score(self):
        """Draw the score to the screen."""
        self.__screen.blit(self.__score_image, self.__score_rect)