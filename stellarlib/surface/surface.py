import pygame


class Surface(object):

    """ Built over pygame.Surface, supposed to wrap it with an interface more suited to
    stellarlib """

    @classmethod
    def _make_copy(cls, surface):

        surface_copy = cls(1, 1)
        surface_copy._surface = surface._surface.copy()
        return surface_copy

    @classmethod
    def from_image(cls, filename):

        image = pygame.image.load(filename)
        surface = cls(1, 1)
        surface._surface = image
        surface.convert()
        return surface

    def __init__(self, w, h):

        self._surface = pygame.Surface((w, h))
        self.convert()

        self.colorkey = None

    def draw(self, target, pos=(0, 0), area=None, special_flags=0):
        """ Surface can draw onto another surface at an option pos argument.
        Can also draw onto a SceneNode in which case draw position is derived
        from the scene tree. """
        target._get_draw_target().blit(self._surface, target._get_draw_pos(pos), area=area,
                                       special_flags=special_flags)

    # **********************
    # Drawable interface ***
    # **********************
    def _get_draw_target(self):
        # _get_draw_target returns a pygame surface to be drawn on
        return self._surface

    def _get_draw_pos(self, pos):
        # returns a 2 integer tuple of draw coord relative to final target surface
        return pos
    # **********************

    def flip(self, vertical_flip=False, horizontal_flip=False):
        self._surface = pygame.transform.flip(self._surface, vertical_flip,
                                              horizontal_flip)

    def horizontal_flip(self):
        self.flip(horizontal_flip=True)

    def vertical_flip(self):
        self.flip(vertical_flip=True)

    def scale(self, factor):
        if factor == 2:
            self._scale_2()
        else:
            self._scale(factor)

    def _scale_2(self):
        self._surface = pygame.transform.scale2x(self._surface)

    def _scale(self, factor):
        self._surface = pygame.transform.scale(self._surface,
                                               (self.get_width() * factor,
                                                self.get_height() * factor))

    def get_rect(self):
        return self._surface.get_rect()

    def convert(self, *args):
        if args:
            self._surface = self._surface.convert(*args)
        else:
            self._surface = self._surface.convert()
        return self

    def copy(self):
        return Surface._make_copy(self)

    def fill(self, color):
        self._surface.fill(color)

    def clear(self, color=(0, 0, 0)):
        self.fill(color)

    # basic getters and setters
    def set_colorkey(self, colorkey, flags=0):
        self.colorkey = colorkey
        self._surface.set_colorkey(colorkey, flags=flags)

    def get_colorkey(self):
        return self.colorkey

    def set_alpha(self, value, flags=0):
        self._surface.set_alpha(value, flags=flags)

    def get_alpha(self):
        return self._surface.get_alpha()

    def get_width(self):
        return self._surface.get_width()

    def get_height(self):
        return self._surface.get_height()

    def get_dimensions(self):
        return self.get_width(), self.get_height()

    # TODO
    def palette_swap(self):
        pass
