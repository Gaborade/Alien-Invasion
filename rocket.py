import pygame


rocket_image = 'images/rocket.bmp'


class Rocket:

    def __init__(self, ai):
        """Initialise the rocket and set its starting position"""

        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        # load rocket image
        self.image = pygame.image.load(rocket_image)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 400

    def blit_image(self):
        """Draw the rocket at its current location"""
        # screen.blit function takes image and position of image as arguments
        self.screen.blit(self.image, (self.rect.x, self.rect.y))



