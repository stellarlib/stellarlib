from .scene import Scene
from .scene_transitions import ExitTransition


class BasicScene(Scene):

    def __init__(self, app):
        Scene.__init__(self, app)

    def get_transition(self):

        return ExitTransition()
