class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings, will eventually be reading from a .txt to save settings
        self.__screen_width = 1920
        self.__screen_height = 1080

        # ship number of lives
        self.__ship_limit = 3

        # how quickly the game (aliens) speeds up with each level.
        self.__speedup_scale = 1.1

        # how quickly the alien point values increase.
        self.__score_scale = 1.5

        # initialize the games dynamic settings.
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the game's dynamic settings (settings that change)."""
        # alien speed
        self.__alien_speed = 1.0

        # alien fleet direction
        self.__fleet_direction = 1 # 1 = right; -1 = left

        # scoring
        self.__alien_points = 50


    def increase_speed(self):
        """Increases the speed of the game and alien points."""
        self.__alien_speed *= self.__speedup_scale

        # increase alien point score scale in int form
        self.__alien_points = int(self.__alien_points * self.__score_scale)


    # Getters
    def get_res_width(self):
        """Returns screen's resolution width"""
        return self.__screen_width

    def get_res_height(self):
        """Returns screen's resolution height"""
        return self.__screen_height

    def get_fleet_direction(self):
        """Returns the fleets direction value."""
        return self.__fleet_direction

    def get_ship_limit(self):
        """Returns number of lives player has."""
        return self.__ship_limit

    def get_alien_speed(self):
        """Returns value of alien speed."""
        return self.__alien_speed

    def get_alien_points(self):
        """Returns value of alien points."""
        return self.__alien_points



    # Setters
    def set_res_width(self, width):
        """Sets the screen's resolution to specified width"""
        # should add ifs to make sure resolution stay in proper format
        # IE: if width == 1280: set_res_height(720)
        self.__screen_width = width

    def set_res_height(self, height):
        """Sets the screen's resolution to specified height"""
        self.__screen_height = height

    def set_fleet_direction(self, direction):
        """Sets the alien fleet's direction."""
        self.__fleet_direction = direction


    



    
