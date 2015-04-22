from nekbot.core import event

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