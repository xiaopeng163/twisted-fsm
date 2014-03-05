#!/usr/bin/env python
# -*- coding:utf-8 -*-

# See LICENSE for details.

""" This is main """

import logging
import argparse

from twisted.internet import reactor
from factory import DemoFactory


def main():

    # init logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s:[%(module)s][%(funcName)s][%(levelname)s]%(message)s')
    ch.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    # parse arguments
    parser = argparse.ArgumentParser(description='This is a demo twsited FSM framework')
    parser.add_argument('-r', '--remote_ip', help='The remote ip address', required=True)
    parser.add_argument('-l', '--local_ip', help='The local ip address', required=True)
    parser.add_argument('-p', '--remote_port', help='the remote server port', required=True)
    args = parser.parse_args()
    # create factory
    demo_factory = DemoFactory(
        server_addr=args.remote_ip,
        local_addr=args.local_ip,
        port=int(args.remote_port)
    )
    demo_factory.automatic_start()

    reactor.run()

if __name__ == "__main__":

    main()