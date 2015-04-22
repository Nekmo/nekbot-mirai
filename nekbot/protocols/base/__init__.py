import threading
from nekbot.core import events

__author__ = 'nekmo'


class Protocol(threading.Thread):
    def __init__(self, nekbot):
        self.nekbot = nekbot
        threading.Thread.__init__(self)
        self.daemon = True

        self.init()

    def propagate(self, event, *args, **kwargs):
        events.propagate(event, self, *args, **kwargs)

    def close(self):
        pass