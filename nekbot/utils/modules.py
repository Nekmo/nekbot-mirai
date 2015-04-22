__author__ = 'nekmo'

def get_module(path):
    return __import__(path, globals(), locals(), [path.split('.')[-1]])

def get_main_class(module, name):
    if hasattr(module, name.capitalize()):
        instance = getattr(module, name.capitalize())
    else:
        raise ImportError
    return instance
