from nekbot.core import event
from nekbot.core.commands import cmds

__author__ = 'nekmo'


@event('message')
def commands_handler(protocol, msg):
    cmds.incoming(msg)