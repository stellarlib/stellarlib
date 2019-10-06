from .surface import Surface
import pygame


class MonoSurface(Surface):

    @classmethod
    def from_image(cls, color):
        return cls(1, 1, color)

    def __init__(self, w, h, color):

        Surface.__init__(self, w, h)
        self.color = color

    def recolor(self, new_color):

        px_array = pygame.PixelArray(self._surface)
        px_array.replace(self.color, new_color)

        self.color = new_color
