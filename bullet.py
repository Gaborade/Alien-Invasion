import pygame
from pygame.sprite import Sprite  # sprite module helps us group related elements in the game and act on all


# grouped elements at once


class Bullet(Sprite):
    """A class to manage bullets fired by ship"""

    def __init__(self, ai):
        Sprite.__init__(self)  # can also use super.__init__(self) but super method is usually used if
        # it involves multiple inheritance
        self.screen = ai.screen
        self.settings = ai.settings
        self.colour = self.settings.bullet_colour


        # create a bullet rect image at (0,0) co-ordinate and then set correct position
        # bullet isn't an image, built bullet from Rect from scratch
        # pygame.Rect() class requires the x- and y- coordinates of rect as well as the width and height of rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # set bullet's rect to be set on the location of the ship's rect midtop position
        # to make it appear as if bullets emerge from the nose of the ship
        self.rect.midtop = ai.ship.rect.midtop

        # store bullet's position as a decimal value
        # self.rect.y cause bullets move along the y-axis.Upwards
        # if bullets moved on a vertical plane like shurikens in an arcade game we would keep the x value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullets up the screen"""
        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
