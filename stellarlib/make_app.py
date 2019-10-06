from .app import Application
from .environment import modify_settings, init


def make_app(main_scene=None, app_settings={}, initial_scene_id='main', _scene_registry={}):

    # first modify any stellarlib settings to suit your application
    modify_settings(**app_settings)

    # then initialize the stellarlib environment
    init()

    # then create your application and it's scenes
    app = Application()

    # set the scene registry of the app and the current scene
    scene_registry = _create_scene_registry(main_scene, initial_scene_id, _scene_registry)
    app.populate(scene_registry, initial_scene_id)

    # return app, can be modified and run
    return app


def _create_scene_registry(main_scene, initial_scene_id, _scene_registry):

    if not main_scene:
        if not _scene_registry or initial_scene_id not in _scene_registry:
            raise Exception('Scene Registry is not set up properly')

    if _scene_registry:
        def test_scene(s):
            # TODO test if value is a valid Scene constructor
            pass
        for _ in map(test_scene, _scene_registry.values()):
            pass

    scene_registry = {}
    scene_registry.update(_scene_registry)

    if main_scene:
        scene_registry[initial_scene_id] = main_scene

    return scene_registry
