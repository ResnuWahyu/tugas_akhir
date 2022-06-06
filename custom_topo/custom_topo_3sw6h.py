#!/usr/bin/env python

"Custom topology"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host
        info( '* Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        info( '* Add hosts\n')
        h1 = self.addHost('h1', ip='10.1.0.1')
        h2 = self.addHost('h2', ip='10.1.0.2')
        h3 = self.addHost('h3', ip='10.2.0.3')
        h4 = self.addHost('h4', ip='10.2.0.4')
        h5 = self.addHost('h5', ip='10.3.0.5')
        h6 = self.addHost('h6', ip='10.3.0.6')
        
        info( '* Add links\n')
        self.addLink(s1, h1, port1=2, port2=1)
        self.addLink(s1, h2, port1=3, port2=1)
        self.addLink(s1, s2, port1=4, port2=2)
        self.addLink(s1, s3, port1=1, port2=3)
        self.addLink(s2, h3, port1=3, port2=1)
        self.addLink(s2, h4, port1=4, port2=1)
        self.addLink(s2, s3, port1=1, port2=4)
        self.addLink(s3, h5, port1=2, port2=1)
        self.addLink(s3, h6, port1=1, port2=1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
