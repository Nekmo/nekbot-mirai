# coding=utf-8
from logging import getLogger

from nekbot.core.exceptions import ProtocolError
from nekbot.utils.modules import get_main_class, get_module
from .base.message import Message
from .base.user import User
from .base.group_chat import GroupChat
from .base import Protocol


__author__ = 'nekmo'

logger = getLogger('nekbot.protocols')

class Protocols(object):
    def __init__(self, nekbot, protocols):
        self.modules = {}  # Módulos de los protocols, no las instancias.
        self.instances = {}  # Instacia ya iniciada dentro del módulo. Ej. "Telegram"
        self.nekbot = nekbot
        self.protocols_list = protocols

    def start(self, protocol):
        logger.info('Starting %s protocol', protocol)
        # Obtengo el módulo del protocolo
        module = get_module('nekbot.protocols.%s' % protocol)
        try:
            # Busco dentro de dicho módulo la "clase principal", aquella con el mismo nombre del
            # módulo, pero que comienza por mayúscula
            instance = get_main_class(module, protocol)
        except ImportError:
            raise ProtocolError('Module %s has does not have a valid instance' % protocol)
        if not hasattr(self, protocol):
            setattr(self, protocol, instance)
        instance = instance(self)
        self.modules[protocol] = module
        self.instances[protocol] = instance
        instance.start()  # Iniciar la instancia

    def start_all(self):
        for protocol in self.protocols_list:
            self.start(protocol)


