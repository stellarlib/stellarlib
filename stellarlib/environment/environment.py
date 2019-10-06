import pygame
import sys
from .settings import Settings


class Environment(object):

    """ The Stellarlib Environment is a singleton that wraps the universal
    aspects of the pygame framework. pygame is initialized here. The display
    surface is initialized and stored here. Default font and an others are held
    here, Etc. """

    def __init__(self, *args, **kwargs):

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))

    @property
    def SCREEN_W(self):
        return Settings.get('SCREEN_W')

    @property
    def SCREEN_H(self):
        return Settings.get('SCREEN_H')

    @property
    def FPS(self):
        return Settings.get('FPS')

    def quit(self):
        pygame.quit()
        sys.exit()

    def refresh_display(self):
        pygame.display.flip()

    def set_window_title(self, title):
        pygame.display.set_caption(title)
