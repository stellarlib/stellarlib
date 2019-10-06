# temp
import pygame
from stellarlib.scene_node import ScreenNode
from stellarlib import make_app


class Scene(object):

    # for basic single scene applications
    @classmethod
    def build_and_run(cls, **kwargs):

        app = make_app(main_scene=cls, **kwargs)
        app.main()

    def __init__(self, app):

        self.app = app
        self.clock = self.app.clock
        self._exit_trigger = False
        self.scene_tree = None

        self._initialize()
        self._show_fps = True

    @property
    def running(self):
        return not self._exit_trigger

    def trigger_exit(self):
        self._exit_trigger = True

    def _initialize(self):
        self.initialize_scene_tree()
        self.populate_scene_tree()
        self.on_start()

    def on_start(self):
        pass

    def on_complete(self):
        print('scene_complete')

    def initialize_scene_tree(self):
        self.scene_tree = ScreenNode(self)

    def populate_scene_tree(self):
        pass

    def main(self):

        #self._initialize()

        while self.running:

            self.handle_input()
            self.update()
            self.draw_display()
            self.tick_frame()
            self.refresh_display()

        self.on_complete()

    def get_transition(self):

        raise NotImplementedError

    # TEMPORARY
    def handle_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.trigger_exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.trigger_exit()

    def update(self):
        self.scene_tree.update()
        self.on_update()

    def on_update(self):
        pass

    def draw_display(self):
        self.scene_tree.draw()

    def tick_frame(self):
        self.clock.tick()

    def refresh_display(self):
        self.app.refresh_display()
        if self._show_fps:
            fps = ''.join((str(self.clock.get_fps()), ' fps'))
            self.app.environment.set_window_title(fps)
