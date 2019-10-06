from .display_node import DisplayNode, Surface


class ScreenNode(DisplayNode):

    def __init__(self, scene):

        self.scene = scene
        env = self.scene.app.environment
        DisplayNode.__init__(self, None, (0, 0), env.SCREEN_W, env.SCREEN_H)
        self._screen = self.init_screen_surface()

    def init_screen_surface(self):
        surface = Surface(self.w, self.h)
        surface._surface = self.scene.app.environment.screen
        return surface

    def draw_self(self, target=None):
        self._surface.draw(self._screen)

    def draw(self):
        self.render_to(self)
