#!/usr/bin/env python
# -*- coding:utf-8 -*-

# See LICENSE for details.

""" This is a demo protocol"""

import logging

from twisted.internet.protocol import Protocol
from twisted.python import failure
from twisted.internet import error


LOG = logging.getLogger()
connectionDone = failure.Failure(error.ConnectionDone())
connectionDone.cleanFailure()


class DemoProtocol(Protocol):

    def __init__(self):

        self.buffer = ''
        self.fsm = None

    def connectionMade(self):
        """
        TCP Conection made
        """
        LOG.info("connection to host %s is connected." % self.transport.getPeer().host)
        self.fsm.connection_made()

    def connectionLost(self, reason=connectionDone):
        """
        TCP conection lost

        :param reason:
        """
        LOG.info("Host %s disconnected. reason: %s " % (self.transport.getPeer().host,
                                                        reason.getErrorMessage()))
        # tell FSM that tcp is lost
        self.fsm.connection_failed()

    def dataReceived(self, data):
        """
        receive data from TCP buffer
        """
        #TODO: to do some process with data received from TCP buffer
        self.buffer += data
        pass
