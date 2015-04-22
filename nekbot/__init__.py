#!/usr/bin/env/python
# coding=utf-8

from nekbot.conf import settings
from nekbot.core import NekBot
from nekbot.protocols import Protocols


__author__ = 'nekmo'

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    NekBot().start().loop()
