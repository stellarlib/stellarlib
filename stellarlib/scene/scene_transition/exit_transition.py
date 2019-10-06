from .scene_transition import SceneTransition
from stellarlib.constants import EXIT


class ExitTransition(SceneTransition):

    def __init__(self):

        SceneTransition.__init__(self, EXIT)
