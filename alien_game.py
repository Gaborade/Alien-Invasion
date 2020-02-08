import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


# from rocket import Rocket

class AlienInvasion:
    """Base class to manage game and all games behaviour"""

    def __init__(self):
        """Initialise game and create game resources"""
        pygame.init()
        # keeping program in a modular manner ensures orthogonality
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # settings will get coordinates for full screen from self.screen
        self.settings.screen_height = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        self.ship = Ship(self)  # because Ship takes AlienInvasion as an argument in ship.py
        self.bullets = pygame.sprite.Group()
        # self.rocket = Rocket(self)
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """watch for keyboard and mouse movements"""
        for event in pygame.event.get():
            # a series of if statements to respond to events by the user
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            # keyup means user has released right arrow key
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        """Responds to key presses"""
        if event.key == pygame.K_RIGHT:
            # when the right arrow key is pressed the moving_right flag boolean is turned to False
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        # enable user to quit by pressing letter 'Q'
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_key_up_events(self, event):
        """Responds to user key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group created by sprite"""
        # giving a limit to amount of bullets allowed on screen
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)  # because AlienInvasion is the second argument to initialise Bullet class
            self.bullets.add(new_bullet)  # .add similar to append in list. Group() works like a list

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # this calls an update for each bullet placed in the group by sprite
        self.bullets.update()

        # delete old bullets that disappear off the top to conserve memory and processing power
        # since they still continue trajectory along the y-axis
        # if bottom of bullet has rect of 0 it means it has disappeared of screen
        for bullet in self.bullets.copy():  # items in a list in a for loop can't be removed so you create a copy
            # to do that
            if bullet.rect.bottom <= 0:
                self.bullets.remove()

    def _update_screen(self):
        """Update images and flip to new screen"""
        # recreate the screen through each iteration through the loop
        self.screen.fill(self.settings.bg_colour)  # note that self.screen.fill wasn't added to the init method
        self.ship.blit_image()
        # self.rocket.blit_image()
        for bullet in self.bullets.sprites():  # bullets.sprites() returns a list of all sprites in the group bullet
            bullet.draw_bullet()  # draw each bullet in the bullets.sprite group

        # make the most recently drawn screen visible as the screen responds to events
        # creates an illusion of smooth movements when there are in fact static pictures
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
