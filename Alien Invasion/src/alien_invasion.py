import sys
from time import sleep

import pygame

from GUI.game_play_screen import GamePlayScreen
from GUI.main_menu import MainMenu
from GUI.game_stats import GameStats
from GUI.scoreboard import Scoreboard
from GUI.pause_menu import PauseMenu
from Sprites.ship import Ship
from Sprites.bullet import Bullet
from Sprites.alien import Alien
from Manager.menu_manager import MenuManager
from settings import Settings



class AlienInvasion:

    def __init__(self):
        pygame.init()

        # makes settings object
        self.__settings = Settings()

        # create screen object
        # self.__screen = pygame.display.set_mode((self.__settings.get_res_width(), self.__settings.get_res_height()))
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # makes full screen resolution
        self.__settings.set_res_width(self.__screen.get_rect().width)
        self.__settings.set_res_height(self.__screen.get_rect().height)


        # creates menu manager object while also passing settings object and screen object for use
        self.__menuManag = MenuManager(self.__settings, self.__screen)

        # creates gamePlayScreen object
        self.__gamePlayScreen = GamePlayScreen(self.__screen)

        # creates ship object with screen object
        self.__ship = Ship(self.__screen)

        # creates bullet object group
        self.__bullets = pygame.sprite.Group()

        # keeps track of how many bullets shot. 0 is temp value, number will be double of amount of aliens spawned.
        self.__total_bullets = 0

        # creates alien object group
        self.__aliens = pygame.sprite.Group()

        # creates alien fleet
        self._create_fleet()

        # create game stats instance to store game stats | passes ship limit.
        self.__stats = GameStats(self.__settings.get_ship_limit())
        # initialize bullet display
        self.__stats.initialize_bullet_display(self.__screen, self.__total_bullets, self.__gamePlayScreen.get_bg_color())

        # create scoreboard
        self.__sb = Scoreboard(self.__screen, self.__stats.get_score(), self.__gamePlayScreen.get_bg_color())

        # runs game
        self.run_game()




    def run_game(self): 
        """Start the main loop for the game."""

        while True:

            # display main menu
            if self.__menuManag.goToPlayScreen() == False:
                self.__menuManag.displayMainMenu()
            # display game play screen    
            elif self.__menuManag.goToPlayScreen() == True: # will be True if user click 'Play' button in Main Menu, false if not.
                # If user pressed 'Play', now BEGIN ALIEN INVASION!

                # check for events
                self._check_for_event()

                if self.__stats.get_game_active_state(): # if True
                    # update ships movement position
                    self.__ship.update()

                    # update bullets and clear bullets out of memory once out of screen
                    self.__update_bullets()

                    # updates aliens movement
                    self.__update_aliens()

                    # re fill alien fleet if empty
                   # self._check_alien_fleet()

                else: # if game active state is false, game over menu will be displayed.

                    # display end game screen
                    self.__menuManag.displayGameOverMenu()

                    # checks what the user is doing in the game over menu.
                    self._check_game_over_menu_actions()
                    
                # update game play screen with images
                self._update_game_play_screen()

            else: # if program some how proceeded to the game play screen without user clicking 'Play' in main menu.
                print(f"ERROR: User didnt click Play, but game proceeded! toPlayScreen = {self.__menuManag.goToPlayScreen()}")



    def _check_for_event(self):
        """Checks for events from user"""

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if a key is pressed down
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            # if a key is released from being held down
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            # if mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events(event)
                


    
    def _check_keydown_events(self, event):
        """Used to manage keydown events from user."""
        # if user presses escape, pop up a pause menu from menu manager
        if event.key == pygame.K_ESCAPE:
            # displays pause menu
            self.__menuManag.displayPauseMenu()

            # if user clicked 'Main Menu' button, reset the game. 
            if self.__menuManag.get_go_to_main_menu() == True:
                self._reset_game_play() # Deletes gameplayscreen, ship, etc objects and remakes them to start game back over when user clicks 'Play' again.
                self.__menuManag.displayMainMenu() # displays mainmenu
            else: # Resume game play.
                # redraws gameplay screen to cover back up paused menu when done in it
                self.__gamePlayScreen.drawScreen() 

        # if user presses 'd' to move ship to the right
        if event.key == pygame.K_d:
            self.__ship.setMovingRight(True) # ship will move right

        # if user presses 'a' to move ship to the left
        if event.key == pygame.K_a:
            self.__ship.setMovingLeft(True) # ship will move left

        # if user presses 'w' to move ship up
        if event.key == pygame.K_w:
            self.__ship.setMovingUp(True) # ship will move up

        # if user presses 's' to move ship down
        if event.key == pygame.K_s:
            self.__ship.setMovingDown(True) # ship will move down

        # if user is holding 'left shift' to go faster
        if event.key == pygame.K_LSHIFT:
            self.__ship.setVelocity(2) # ship velocity increased to 2



    def _check_keyup_events(self, event):
        """Used to manage keyup events from user."""
        # if user was holding down 'd' to move ship to the right
        if event.key == pygame.K_d:
            self.__ship.setMovingRight(False) # ship will stop moving right

        # if user was holding down 'a' to move ship to the left
        if event.key == pygame.K_a:
            self.__ship.setMovingLeft(False) # ship will stop moving left

        # if user was holding down 'w' to move ship up
        if event.key == pygame.K_w:
            self.__ship.setMovingUp(False) # ship will stop moving up

        # if user was holding down 's' to move ship down
        if event.key == pygame.K_s:
            self.__ship.setMovingDown(False) # ship will stop moving down

        # if user was holding down 'left shift' to go faster
        if event.key == pygame.K_LSHIFT:
            self.__ship.setVelocity(1) # ship velocity decreased back to 1



    def _check_mouse_events(self, event):
        """Used to manage mouse button events from user."""
        # used to distinguish if left or right mouse click was pressed.
        left = 1
        right = 3

        # if user pressed left mouse button to fire bullet.
        if event.button == left: # left = 1
            self._fire_bullet()


 #   def _check_alien_fleet(self):
 #       """Checks to see if alien fleet is empty, if so, make new fleet."""
 #       if not self.__aliens: # checks if aliens group is empty, will be false.
 #           self._create_fleet()
        #    self.__settings.increase_speed()


    def _check_game_over_menu_actions(self):
        """Checks what buttons the user is pressing in the game over menu."""
        # if user clicked 'Main Menu' button, reset the game. 
        if self.__menuManag.get_go_to_main_menu() == True:
            self._reset_game_play() # Deletes gameplayscreen, ship, etc objects and remakes them to start game back over when user clicks 'Play' again.
            self.__menuManag.displayMainMenu() # displays mainmenu
        elif self.__menuManag.playAgain(): # if player clicks 'Play again' button
            # reset the game.
            self._reset_game_play()



    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if self.__total_bullets > 0:
            new_bullet = Bullet(self.__screen, self.__ship)
            self.__bullets.add(new_bullet)
            self.__total_bullets -= 1

        # preps display for bullets remaing.
        self.__stats.prep_bullets_display(self.__total_bullets)



    def __update_aliens(self):
        """
        Check if the fleet is at an edge.
        then update the positions of all aliens in the fleet.
        """
        # passes fleet direction from settings.py. no need to pass the entire settings object.
        self._check_fleet_edges()
        self.__aliens.update(self.__settings.get_fleet_direction())

        # look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.__ship, self.__aliens):
            self._ship_hit()

        # check if aliens have reached bottom of screen.
        self._check_aliens_bottom()
            



    def __update_bullets(self):
        """updates bullets and clears out of memory once they're out of the screen."""
        # updates bullets position
        self.__bullets.update()

        for bullet in self.__bullets.copy(): # creates copy of bullets group, cant loop and remove objects from same list at same time.
            if bullet.getRect().bottom <= 0 or bullet.getRect().left >= self.__screen.get_rect().width or bullet.getRect().right <= 0: # reached top of screen or sides of the screen
                self.__bullets.remove(bullet)

        # check bullet collisions with aliens.
        self._check_bullet_alien_collision()

        



    def _create_fleet(self):
        """Create the fleet of aliens."""
        # make an alien and find the number of aliens in a row.
        # spacing between each alien is equal to one alien width.
        alien = Alien(self.__screen, self.__settings.get_alien_speed())
        alien_width = alien.getWidth()
        alien_height = alien.getHeight()
        available_space_x = self.__settings.get_res_width() - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen.
        ship_height = self.__ship.getRect().height
        available_space_y = (self.__settings.get_res_height() - ( 8 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # find total bullets player gets, double of fleet size
        self.__total_bullets = (number_aliens_x * number_rows) * 2 # used to manage how many bullets player can shoot, based off alien amount spawned.

        # create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # create an alien and place it in the row
                self._create_alien(alien_number, row_number)
            


    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self.__screen, self.__settings.get_alien_speed())
        alien_width = alien.getWidth()
        alien_height = alien.getHeight()
        alien.setX(alien_width + 2 * alien_width * alien_number) # set X of next alien
        alien.rect.x = alien.getX()
        alien.rect.y = alien.getHeight() + 2 * alien.getHeight() * row_number
        self.__aliens.add(alien)



    def _check_fleet_edges(self):
        """Respond appropiately if any aliens have reached an edge."""
        for alien in self.__aliens.sprites():
            if alien.check_edges(): # if returns true
                self._change_fleet_direction()
                break

        

    def _change_fleet_direction(self):
        """Changes the fleet direction."""
        # for dropping the fleet
        for alien in self.__aliens.sprites():
            alien.rect.y += alien.getDropSpeed() 

        # change the X direction of fleet
        self.__settings.set_fleet_direction(self.__settings.get_fleet_direction() * -1)



    def _check_bullet_alien_collision(self):
        """Checks and responds to bullet-alien collisions."""
        # remove any alien and bullet that have collided.
        # check for any bullets that have hit aliens.
        # get rid of bullet and alien, if so.
        collisions = pygame.sprite.groupcollide(self.__bullets, self.__aliens, True, True)

        # update score if player hit an alien
        if collisions: # if bullets have hit aliens.
            for aliens in collisions.values(): # for each alien hit by the bullet. Makes sure to give points if a single bullet takes out more than one alien.
                self.__stats.increase_score(self.__settings.get_alien_points() * len(aliens))
            self.__sb.prep_score(self.__stats.get_score())

        # if no aliens, make new fleet of aliens appear and get rid of existing bullets
        if not self.__aliens: # will be false if empty, all aliens shot down.
            # Destroy existing bullets and create new fleet.
            self.__bullets.empty()
            self.__settings.increase_speed() # increase speed of aliens for new level.
            self._create_fleet()
            self.__stats.prep_bullets_display(self.__total_bullets) # adjust bullet display to be accurate with new wave
            



    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        # gets screen rect
        screen_rect = self.__screen.get_rect()

        # goes through each alien to see if it has reach bottom of the screen.
        for alien in self.__aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship got hit.
                self._ship_hit()
                break # only needs to find one alien hitting bottom.



    def _ship_hit(self):
        """Responds to the ship being hit by an alien."""

        if self.__stats.get_ships_left() > 0:
            # subtract 1 from ships left.
            self.__stats.set_ships_left(self.__stats.get_ships_left() - 1)

            # get rid of any remaining aliens and bullets
            self.__aliens.empty()
            self.__bullets.empty()

            # create new fleet and center the ship.
            self._create_fleet()
            self.__ship.center_ship()

            # pause for a few for player to adjust to what just happened.
            sleep(0.5)

        else: # if player has been hit when they are on their last life.
            self.__stats.has_more_lives(False)

    
    def _update_game_play_screen(self):
        """Update images on the game play screen and flip to new screen."""

        # Draws the game play screen
        self.__gamePlayScreen.drawScreen()

        # draws ship to screen
        self.__ship.blitme()

        # draw bullets from bullet list Group
        for bullet in self.__bullets.sprites():
            bullet.draw_bullet()

        # draws alien
        self.__aliens.draw(self.__screen)

        # draws score info.
        self.__sb.show_score()

        # draws bullets remain
        self.__stats.show_bullets_remaining()

        # Make the most recently drawn screen visible.
        pygame.display.flip()



    def _reset_game_play(self):
        """Resets the game for next time user clicks 'Play'."""
        del self.__gamePlayScreen # deletes gameplayscreen object
        del self.__ship # deletes ship object
        self.__aliens.empty() # empties current alien fleet.
        self.__bullets.empty() # empties bullets
        self.__stats.reset_stats() # resets stats and game_active back to True.
        self.__sb.prep_score(self.__stats.get_score()) # resets score back to 0.
        self.__settings.initialize_dynamic_settings() # resets dynamic settings.
        self.__gamePlayScreen = GamePlayScreen(self.__screen) # reinitiates new gameplayscreen
        self.__ship = Ship(self.__screen) # reinitiates new ship
        self._create_fleet() # recreates the first fleet       



if __name__ == '__main__':

        # Starts the game
        ai = AlienInvasion()