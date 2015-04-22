__author__ = 'nekmo'

class User(object):

    def __init__(self, protocol, username, id=None):
        self.protocol, self.username, self.id = protocol, username, id

    def __repr__(self):
        return '<%s %s id:%s>' % (self.__class__, self.username, self.id)

    def __str__(self):
        return self.username