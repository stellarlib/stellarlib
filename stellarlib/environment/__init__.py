from .environment import Environment
from .settings import Settings


class Initialization(object):

    _INITIALIZED = False
    STELLARLIB_ENV = None


def is_initialized():
    return Initialization._INITIALIZED


def modify_settings(**kwargs):

    if is_initialized():
        raise Exception('Stellarlib is already initialized')

    Settings.modify(**kwargs)


def init(*args, **kwargs):

    if is_initialized():
        raise Exception('Stellarlib is already initialized')
    Initialization._INITIALIZED = True

    env = get_environment(*args, **kwargs)

    return env


def get_environment(*args, **kwargs):

    if not is_initialized():
        raise Exception('Stellarlib is not initialized')

    if Initialization.STELLARLIB_ENV is None:
        Initialization.STELLARLIB_ENV = Environment(*args, **kwargs)

    return Initialization.STELLARLIB_ENV
