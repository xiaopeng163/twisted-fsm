#!/usr/bin/env python
# -*- coding:utf-8 -*-

# See LICENSE for details.

""" timer"""

from twisted.internet import reactor, error


class Timer(object):
    """
    Timer class with a slightly different Timer interface than the
    Twisted DelayedCall interface
    """

    def __init__(self, call_able):

        self.delayed_call = None
        self.callable = call_able

    def cancel(self):

        """Cancels the timer if it was running, does nothing otherwise"""

        try:
            self.delayed_call.cancel()
        except (AttributeError, error.AlreadyCalled, error.AlreadyCancelled):
            pass

    def reset(self, seconds_fromnow):
        """Resets an already running timer, or starts it if it wasn't running.

        :param seconds_fromnow : restart timer
        """

        try:
            self.delayed_call.reset(seconds_fromnow)
        except (AttributeError, error.AlreadyCalled, error.AlreadyCancelled):
            self.delayed_call = reactor.callLater(seconds_fromnow, self.callable)

    def active(self):
        """Returns True if the timer was running, False otherwise."""

        try:
            return self.delayedCall.active()
        except AttributeError:
            return False