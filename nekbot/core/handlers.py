from nekbot.core import event
from nekbot.core.commands import cmds

__author__ = 'nekmo'


@event('message')
def print_message(protocol, msg):
    if msg.body == 'Ping':
        msg.reply('Pong')

@event('message')
def print_message(protocol, msg):
    import platform
    version = platform.python_version()
    if msg.body == '!about':
        msg.reply('NekBot Mirai | El bot modular multiprotocolo | Funcionando bajo Python %s' % version)

@event('message')
def commands_handler(protocol, msg):
    cmds.incoming(msg)