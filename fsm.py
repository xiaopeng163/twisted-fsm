#!/usr/bin/env python
# -*- coding:utf-8 -*-

# See LICENSE for details.

""" This a demo FSM"""


import logging

from timer import Timer
from constants import CONNECT_RETRY_TIME

LOG = logging.getLogger()


class FSM(object):

    protocol = None
    state = False

    def __init__(self, factory=None, protocol=None):

        self.factory = factory
        self.protocl = protocol
        self.state = False
        self.connect_retry_time = CONNECT_RETRY_TIME
        self.connect_retry_timer = Timer(self.connect_retry_event)

    def __setattr__(self, name, value):

        if name == 'state' and value != getattr(self, name):
            LOG.info("State is now:%s" % value)

        super(FSM, self).__setattr__(name, value)

    def automatic_start(self):
        """
        automatic start
        """
        LOG.debug('automatic start')
        self.connect_retry_timer.reset(self.connect_retry_time)
        return True

    def connect_retry_event(self):

        """
        connect retry
        """
        LOG.debug('connect retry')
        self.connect_retry_timer.reset(self.connect_retry_time)
        if self.factory:
            self.factory.connect_retry()

    def keep_alive_time_event(self):
        pass

    def connection_made(self):

        self.connect_retry_timer.cancel()
        self.state = True

    def connection_failed(self):

        self.connect_retry_timer.reset(self.connect_retry_time)
        self.state = False