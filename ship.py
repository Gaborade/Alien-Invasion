import pygame

ship_image = 'images/ship.bmp'


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai):  # the other parameter is the alien invasion class
        """Initialise the ship and set its starting position"""
        self.screen = ai.screen
        self.settings = ai.settings
        self.screen_rect = ai.screen.get_rect()

        # load ship image and get rectangle position
        self.image = pygame.image.load(ship_image)
        self.rect = self.image.get_rect()
        # ship's rect image is put at the midbottom of the screen rect
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blit_image(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update ship position based on movement flag"""
        # if blocks rather than an if and an elif so that rect.x can increase and decrease
        # when both right and left arrow keys are held down
        # update ship's x value and not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:  # self.rect.right refers to the x
            # co-ordinate at the right edge of image self.rect.right needs to be lesser than x co-ordinate of the
            # screen so the image doesn't disappear when moved to the right edge of the screen
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            #  self.rect.left of ship image should be greater than the left edge of the screen rect of x which is 0
            self.x -= self.settings.ship_speed

        # update self.rect.x value based on self.x
        # did all this decimal bullshit cause rect takes only integer values
        self.rect.x = self.x
