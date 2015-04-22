__author__ = 'nekmo'

class Message(object):

    def __init__(self, protocol, body, user, group=None):
        self.protocol, self.body, self.user, self.group = protocol, body, user, group

    def reply(self, body):
        pass

    def __str__(self):
        return self.body