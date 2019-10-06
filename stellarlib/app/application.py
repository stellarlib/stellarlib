from stellarlib.environment import get_environment
from stellarlib.constants import EXIT
from .clock import Clock


class Application(object):

    def __init__(self):

        self.environment = get_environment()
        self.current_scene = None
        self.clock = Clock(self)
        self.scene_registry = {None: lambda x: x}

    def main(self):

        while self.current_scene:

            self.current_scene.main()

            self.current_scene = self.load_next_scene()

        self.environment.quit()

    def load_next_scene(self):

        transition = self.current_scene.get_transition()

        if transition.value == EXIT:
            return None
        else:
            return self._load_next_scene(transition)

    def _load_next_scene(self, transition):
        next_scene = self.scene_registry.get(transition.value)
        return next_scene(
                           self,
                           *transition.args,
                           **transition.kwargs
                          )

    def register_scene(self, scene_id, scene_constructor):
        self.scene_registry[scene_id] = scene_constructor

    def set_initial_scene(self, scene_id):

        assert self.current_scene is None
        self.current_scene = self.scene_registry.get(scene_id)(self)

    def populate(self, scene_registry, initial_scene_id):
        for scene in scene_registry.items():
            self.register_scene(*scene)

        self.set_initial_scene(initial_scene_id)

    def refresh_display(self):
        self.environment.refresh_display()
