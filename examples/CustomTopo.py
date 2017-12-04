
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
#from mininet.node import Node
from mininet.link import TCLink
#from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class Traffic_Shaping( Topo ): 

    def __init__( self ):
        "Create Network topology for to show segment SDWAN Network"

        # Initialize topology
        Topo.__init__( self )

        # Hosts and Switches
        
        h1   =  self.addHost( 'h1',mac='00:00:00:00:00:41',ip='192.168.1.1/24')
        h2   =  self.addHost( 'h2',mac='00:00:00:00:00:42',ip='192.168.1.2/24')
        '''h3   =  self.addHost( 'h3',mac='00:00:00:00:00:44',ip='192.168.1.4/24')
        h4   =  self.addHost( 'h4',mac='00:00:00:00:00:46',ip='192.168.1.6/24')
        h5   =  self.addHost( 'h5',mac='00:00:00:00:00:48',ip='192.168.1.8/24')
        h6   =  self.addHost( 'h6',mac='00:00:00:00:00:50',ip='192.168.1.10/24')
        h7   =  self.addHost( 'h7',mac='00:00:00:00:00:52',ip='192.168.1.12/24')'''
        
        s1   =  self.addSwitch('s1')
        s2   =  self.addSwitch('s2')
        s3   =  self.addSwitch('s3')
      '''  s4   =  self.addSwitch('s4')
        s5   =  self.addSwitch('s5')
        s6   =  self.addSwitch('s6')'''
    
     
        # Add links
        # self.addLink( h1, s1 )
        # self.addLink( s1, s6 )
        # self.addLink( s1, s2 )
        # self.addLink( s2, h2 )
        # self.addLink( s2, s3 )
        # self.addLink( s3, h7 )
        # self.addLink( s3, s4 )
        # self.addLink( s4, h6 )
        # self.addLink( s5, s4 )
        # self.addLink( s5, h5 )
        # self.addLink( s5, h4 )
        # self.addLink( s6, s5 )
        # self.addLink( s6, h3 )
        
        self.addLink( h1, s2 )
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s1 )
        self.addLink( h2, s3 )

        
        '''self.addLink( h2, h4, bw=10, delay='10ms', max_queue_size=4000 )
        self.addLink( h3, h4, bw=10, delay='10ms', max_queue_size=4000 )
        '''
        
topos = { 'trafficshape': ( lambda: Traffic_Shaping() ) }


def run():
    "Test linux router"
    topo = Traffic_Shaping()
    net = Mininet( topo=topo, link=TCLink, controller=None )  
    #net.build()
    
    
    
    info( '*** Adding controller\n' )
    c0=net.addController( 'c0', controller=RemoteController, ip='192.168.56.101',port=6633)
    
    # net.build()
    
    net.start()
    
    print "Creation of SD WAN is done"
    # h1, h2, h3, h4, h5, h6, h7 = net.getNodeByName('h1','h2','h3','h4','h5','h6','h7')
    
    # info( '*** Assigning IP address for eth1 interfaces\n')
    # # h2.cmd('ifconfig h2-eth1 192.168.1.3 netmask 255.255.255.0')
    # # h3.cmd('ifconfig h3-eth1 192.168.1.5 netmask 255.255.255.0')
  
  
    # info( '*** Creating Route add \n')
    # # h1.cmd('route add default gw 192.168.12.2')
    # # h4.cmd('route add default gw 192.168.23.2')
    
    # info( '*** Enabling IP forwarding \n')
    # # h2.cmd('sysctl net.ipv4.ip_forward=1')
    # # h3.cmd('sysctl net.ipv4.ip_forward=1') 
    # # h4.cmd('sysctl net.ipv4.ip_forward=1') #added extra
    
    # info('*** Adding additional interface and configuring on controller\n')
    # net.addLink( h2, c0)
    # net.addLink( h3, c0)
    # net.addLink( h4, c0)
    
    # #creating bridge at controller for http connection to h2 and h3
    # c0.cmd('brctl addbr bridgec0')
    # c0.cmd('ifconfig c0-eth0 0')
    # c0.cmd ('ifconfig c0-eth1 0')
    # c0.cmd ('ifconfig c0-eth2 0')
    # c0.cmd('brctl addif bridgec0 c0-eth0')
    # c0.cmd('brctl addif bridgec0 c0-eth1')
    # c0.cmd('brctl addif bridgec0 c0-eth2')
    # c0.cmd('ifconfig bridgec0 10.0.0.1 netmask 255.255.0.0 up') 
    
    # h2.cmd('ifconfig h2-eth1 10.0.0.2 netmask 255.255.0.0')
    # h3.cmd('ifconfig h3-eth1 10.0.0.3 netmask 255.255.0.0')
    # h4.cmd('ifconfig h4-eth1 10.0.0.4 netmask 255.255.0.0')
    
    # # run the python server silent on h2 h3 h4
    
    # h2.cmd('python -m SimpleHTTPServer 80 &')
    # h3.cmd('python -m SimpleHTTPServer 80 &')
    # h4.cmd('python -m SimpleHTTPServer 80 &')
    
    # h2.cmd('python serverinfo_h2.py &')
    # h3.cmd('python serverinfo_h3.py &')
    # h4.cmd('python serverinfo_h4.py &')
    
    """
    c0.cmd('ifconfig c0-eth0 10.0.0.1 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth2 10.0.0.2 netmask 255.255.255.0')
    
    c0.cmd('ifconfig c0-eth1 10.0.0.3 netmask 255.255.255.0')  
    h3.cmd('ifconfig h3-eth2 10.0.0.4 netmask 255.255.255.0')
    
    info( '*** Creating Route add \n')
    c0.cmd('route add 10.0.0.1 gw 10.0.0.2')
    h2.cmd('route add 10.0.0.2 gw 10.0.0.1')
    
    c0.cmd('route add 10.0.0.3 gw 10.0.0.4')
    h3.cmd('route add 10.0.0.4 gw 10.0.0.3') 
    """
    
    #h4.cmd('ifconfig h4-eth1 0.0.0.0')
    #h4.cmd('ifconfig h4-eth0 0.0.0.0')
    """
    # Creating bridge in H2
    h2.cmd('brctl addbr mybridge')
    h2.cmd('ifconfig h2-eth0 0')
    h2.cmd ('ifconfig h2-eth1 0')
    h2.cmd('brctl addif mybridge h2-eth0')
    h2.cmd('brctl addif mybridge h2-eth1')
    h2.cmd('ifconfig mybridge 192.168.1.2 netmask 255.255.0.0 up')
    
    # Creating bridge in H3
    h3.cmd('brctl addbr bridge')
    h3.cmd('ifconfig h3-eth0 0')
    h3.cmd ('ifconfig h3-eth1 0')
    h3.cmd('brctl addif bridge h3-eth0')
    h3.cmd('brctl addif bridge h3-eth1')
    h3.cmd('ifconfig bridge 192.168.1.4 netmask 255.255.0.0 up') 

    # Creating bridge in H4
    h4.cmd('brctl addbr bridgeh4')
    h4.cmd('ifconfig h4-eth0 0')
    h4.cmd ('ifconfig h4-eth1 0')
    h4.cmd('brctl addif bridgeh4 h4-eth0')
    h4.cmd('brctl addif bridgeh4 h4-eth1')
    h4.cmd('ifconfig bridgeh4 192.168.1.6 netmask 255.255.0.0 up') 
    
    
    # Creating Bond Not used 
    h4.cmd('modprobe bonding')
    h4.cmd('ip link add bond0 type bond')
    h4.cmd('ip link set bond0 address 02:01:02:03:04:08')
    h4.cmd('ip link set h4-eth0 down')
    h4.cmd('ip link set h4-eth0 address 00:00:00:00:00:11')
    h4.cmd('ip link set h4-eth0 master bond0')
    h4.cmd('ip link set h4-eth1 down')
    h4.cmd('ip link set h4-eth1 address 00:00:00:00:00:12')
    h4.cmd('ip link set h4-eth1 master bond0')
    h4.cmd('ip addr add 192.168.1.6/24 dev bond0')
    h4.cmd('ip addr del 192.168.1.6/24 dev h4-eth0')   
    h4.cmd('ip link set bond0 up')'''
    
   # info('*** Ping test from h1 to h4 \n')
   # print h1.cmd('ping -c 1 192.168.23.4')
    
   # info('*** IPERF test from h1 to h4 \n')
   # #net.iperf( ( h1, h4 ), l4Type='TCP' )
    

    # info('*** Ping test for controller \n')
    #print c0.cmd('ping -c 4 10.0.0.2')
    #print h2.cmd('ping -c 4 10.0.0.1')
    
    """
 
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()