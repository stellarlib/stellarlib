

class Settings(object):

    """ Settings is a container for the default engine settings of Stellarlib.
    they should be modified before stellarlib is initialized using the
    modify_settings method at the base level of stellarlib."""

    _settings = {
        'SCREEN_W': 800,
        'SCREEN_H': 600,
        'FPS': 60,
    }

    @classmethod
    def modify(cls, **kwargs):
        for k, v in kwargs.items():
            assert k in cls._settings
            cls._settings[k] = v

    @classmethod
    def get(cls, key):
        return cls._settings.get(key)
