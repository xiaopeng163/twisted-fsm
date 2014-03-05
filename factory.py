#!/usr/bin/env python
# -*- coding:utf-8 -*-

# See LICENSE for details.

""" This a demo factory """

import logging
from twisted.internet import protocol
from twisted.internet import reactor

from protocol import DemoProtocol
from fsm import FSM

LOG = logging.getLogger()


class BaseFactory(protocol.Factory):

    """Base factory for creating a demo protocol instances."""

    protocol = DemoProtocol
    FSM = FSM

    def __init__(self):
        pass

    def buildProtocol(self, addr):

        """Builds a Base instance.

        :param addr : address used for buliding protocol.
        """
        return protocol.Factory.buildProtocol(self, addr)

    def startedConnecting(self, connector):

        """Called when a connection attempt has been initiated.

        :param connector : Twisted connector
        """
        LOG.debug('start connecting..')
        pass

    def clientConnectionLost(self, connector, reason):

        """ Called when a TCP client connection was lost.

        :param connector : Twisted connector
        :param reason : connection faied reason.
        """
        LOG.info("Client connection lost:%s" % reason.getErrorMessage())


class DemoFactory(BaseFactory):
    """Base factory for creating demo protocol instances."""

    def __init__(self, server_addr, local_addr, port):

        """
        init
        """
        LOG.info('initial demo Factory!')
        BaseFactory.__init__(self)
        self.server_addr = server_addr
        self.local_addr = local_addr
        self.port = port
        self.fsm = BaseFactory.FSM(self)

    def buildProtocol(self, addr):
        """Builds a channle Protocol instance.
        """
        LOG.debug('build protocol')
        p = BaseFactory.buildProtocol(self, addr)
        if p is not None:
            self._init_protocol(p)
        return p

    def _init_protocol(self, protocol):

        """Initializes a Protocol instance

        :param protocol: twisted Protocol
        """
        LOG.debug('init protocol')
        protocol.factory = self

        # Hand over the FSM
        protocol.fsm = self.fsm
        protocol.fsm.protocol = protocol

    def automatic_start(self):

        if self.fsm.automatic_start():
            self.connect()

    def connect_retry(self):
        self.connect()

    def connect(self):

        """Initiates a TCP client connection to the channel server.
        """
        # DEBUG
        LOG.info("(Re)connect to channel server %s" % self.server_addr)
        reactor.connectTCP(host=self.server_addr,
                           port=self.port,
                           factory=self,
                           bindAddress=(self.local_addr, 0))

    def clientConnectionFailed(self, connector, reason):

        """Called when the outgoing connection failed.

        :param connector: Twisted connector
        :param reason: connection failed reason
        """

        LOG.info('connection failed: %s' % reason.getErrorMessage())
        try:
            self.fsm.connection_failed()
        except Exception as e:
            LOG.error(e)