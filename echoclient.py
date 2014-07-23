#!/usr/bin/env python
# encoding: utf-8
"""
echoclient.py

Created by Terry Bates on 2014-07-16.
Copyright (c) 2014 LinkedIn. All rights reserved.
"""

from twisted.internet import protocol, reactor


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello World!")
    
    def dataReceived(self, data):
        print "Server said", data
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()
        
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        reactor.stop()


def main():
    reactor.connectTCP("localhost",8000, EchoFactory())
    reactor.run()


if __name__ == '__main__':
	main()

