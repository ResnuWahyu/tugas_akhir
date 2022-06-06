# Custom Topology 2sw2h
## Membuat program 2sw2h
- Buat file dengan nama custom_topo_2sw2h.py
```sh
nano custom_topo_2sw2h.py
```
- Masukkan kode program dibawah kedalam file tersebut
```python
#!/usr/bin/env python
" Custom Topology "
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

# Tambahkan Switch
info( '*** Add switches\n')
s1 = self.addSwitch('s1')
s2 = self.addSwitch('s2')
# Tambahkan Host
info( '*** Add hosts\n')
h1 = self.addHost('h1', ip='10.1.0.1/24')
h2 = self.addHost('h2', ip='10.1.0.2/24')
# Tambahkan Node
info( '*** Add links\n’)
self.addLink(s1, h1, port1=1, port2=1)
self.addLink(s1, s2, port1=2, port2=1)
self.addLink(s2, h2, port1=2, port2=1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
```
## Menjalankan program dan menambahkan flow
- Jalankan mininet tanpa controller
```sh
sudo mn --controller=none --custom custom_topo_2sw2h.py --topo mytopo --mac --arp
```
- Buatlah flow agar host bisa terhubung
```sh
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=1,action=output:2"
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=2,action=output:1"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=1,action=output:2"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=2,action=output:1“
```
- Lakukan tes koneksi
```sh
h1 ping -c2 h2
```
Jika sudah berhasil melakukan koneksi, maka program dan flow yang ditambahkan sudah benar dan berjalan dengan baik

# Custom Topology 3sw6h
## Membuat program 3sw6h
- Buat file dengan nama custom_topo_3sw6h.py
```sh
nano custom_topo_3sw6h.py
```
- Masukkan kode program dibawah kedalam file tersebut
```python
#!/usr/bin/env python

"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def _init_( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo._init_( self )

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
```
## Menjalankan program dan menambahkan flow
- Jalankan mininet tanpa controller
```sh
sudo mn --controller=none --custom custom_topo_3sw6h.py --topo mytopo --mac --arp
```
- Buatlah flow agar host bisa terhubung
```sh
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=1,action=output:2,3,4"
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=2,action=output:1,3,4"
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=3,action=output:1,2,4"
sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=4,action=output:1,2,3"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=1,action=output:2,3,4"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=2,action=output:1,3,4"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=3,action=output:1,2,4"
sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=4,action=output:1,2,3"
sh ovs-ofctl add-flow s3 -O OpenFlow13 "in_port=1,action=output:2,3,4"
sh ovs-ofctl add-flow s3 -O OpenFlow13 "in_port=2,action=output:1,3,4"
sh ovs-ofctl add-flow s3 -O OpenFlow13 "in_port=3,action=output:1,2,4"
sh ovs-ofctl add-flow s3 -O OpenFlow13 "in_port=4,action=output:1,2,3"
```
- Lakukan tes koneksi
```sh
h1 ping -c2 h3
```
Jika sudah berhasil melakukan koneksi, maka program dan flow yang ditambahkan sudah benar dan berjalan dengan baik
