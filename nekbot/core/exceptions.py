# coding=utf-8
from nekbot.utils.strings import human_join

__author__ = 'nekmo'

class ProtocolError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class PrintableException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class InvalidArgument(PrintableException):
    def __init__(self, msg, value, pos=None):
        self.msg, self.value, self.pos = msg, value, pos

    def one_argument(self):
        body = 'El argumento '
        if self.pos is not None:
            body += 'en la posición %s ' % (self.pos + 1)
        body += 'con valor "%s", no es válido.' % self.value
        return body

    def several_arguments(self):
        positions = self.pos if self.pos else []
        body = 'Los argumentos '
        args = []
        for i, value in enumerate(self.value):
            arg = '"%s"' % value
            if len(self.pos) >= i:
                arg += ' (posición %s)' % (positions[i] + 1)
            args.append(arg)
        body += human_join(args, 'y')
        body += ' no son válidos.'
        return body

    def __str__(self):
        if isinstance(self.value, (list, tuple)):
            body = self.several_arguments()
        else:
            body = self.one_argument()
        return '%s %s' % (body, self.msg)


    def __repr__(self):
        return '<InvalidArgument "%s">' % str(self)