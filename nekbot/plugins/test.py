# coding=utf-8
from types import IntType
from nekbot.core.commands import command
from nekbot.core.commands.control import control
from nekbot.core.commands.temp import TempRegex
from nekbot.core.exceptions import PrintableException

__author__ = 'nekmo'

@command('argnumber', int)
def argnumber(msg, number):
    assert type(number) is IntType
    msg.reply('Entregado: %i' % number)

@command
def args(msg, *args):
    msg.reply('Entregado: %s' % ', '.join(args))

@command
def kwargnumber(msg, number=10):
    assert type(number) is IntType
    return 'Entregado: %i' % number

@command
def privatemsg(msg):
    msg.user.send_message('Un mensaje privado')

@command
def publicmsg(msg):
    msg.groupchat.send_message('Un mensaje público')

@command
def test_temp_regex(msg):
    msg.reply('Elija: [Sn]')
    temp = TempRegex(msg.protocol, '^(S|s|N|n)$', timeout=5)
    response = temp.read().next()
    msg.reply('Usted ha dicho: %s' % response.match[0])

@command
@control('root')
def need_root(msg):
    return 'Hola jefe!'

@command
@control('spam')
def need_spam(msg):
    return 'Spam! Spam! Spam!!'

@command
def raise_printable_exception(msg):
    raise PrintableException("nobody's specs the spanish inquisition!")

@command
def raise_exception(msg):
    raise Exception
