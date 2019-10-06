from .scene_node import SceneNode
from stellarlib.surface import Surface
# from stellarlib.utilities.random.random_color import random_color


class DisplayNode(SceneNode):

    def __init__(self, parent, pos, width, height, auto_refresh=True):

        SceneNode.__init__(self, parent, pos)
        self.w = width
        self.h = height
        self.clear_color = (0, 0, 0)
        self.auto_refresh = auto_refresh

        self._surface = self.init_surface()

    def init_surface(self):
        return Surface(self.w, self.h)

    def _get_draw_target(self):
        return self._surface._get_draw_target()

    def get_display(self):
        return self

    def update(self):

        if self.auto_refresh:
            self.refresh()

        self.position.update()
        [component.update() for component in self.components]
        [child.update() for child in self.children]

    def render_to(self, target):

        [component.draw(self) for component in self.components]
        [child.render_to(self) for child in self.children]

        self.draw_self(target)

    def draw_self(self, target):
        """ Draws the display's surface onto the target surface """
        self._surface.draw(target, self.relative_pos(target))

    def refresh(self):
        self._surface.clear(self.clear_color)
