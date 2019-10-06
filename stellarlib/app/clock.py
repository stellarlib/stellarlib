import pygame


class Clock(object):

    def __init__(self, app):

        self._clock = pygame.time.Clock()
        self.FPS = app.environment.FPS

    def tick(self):

        self._clock.tick(self.FPS)

    def get_fps(self):

        return round(self._clock.get_fps(), 1)
