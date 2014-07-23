#!/usr/bin/env python
# encoding: utf-8
"""
echoserver.py

Created by Terry Bates on 2014-07-16.
Copyright (c) 2014 LinkedIn. All rights reserved.
"""

from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


def main():
    reactor.listenTCP(8000, EchoFactory())
    reactor.run()


if __name__ == '__main__':
	main()

