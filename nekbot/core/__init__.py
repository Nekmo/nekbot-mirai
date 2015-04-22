from logging import getLogger
from threading import Semaphore
from nekbot.plugins import Plugins

from .signals import events, event
from nekbot.protocols import Protocols
from nekbot.conf import settings
from . import handlers


__author__ = 'nekmo'
logger = getLogger('nekbot')


class NekBot(object):
    def __init__(self):
        self.semaphore = Semaphore()
        self.protocols = Protocols(self, settings.PROTOCOLS)
        self.plugins = Plugins(self, settings.PLUGINS)

    def start(self):
        self.start_protocols()
        self.start_plugins()
        return self

    def start_protocols(self):
        self.protocols.start_all()

    def start_plugins(self):
        self.plugins.start_all()

    def loop(self):
        logger.info('Everything has started')
        self.semaphore.acquire()