

from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

      
        Topo.__init__( self )

        host_h1 = self.addHost( 'h1' )
        host_h2 = self.addHost( 'h2' )
        host_h3 = self.addHost( 'h3' )
        host_h4 = self.addHost( 'h4' )
        host_h5 = self.addHost( 'h5' )
        host_h6 = self.addHost( 'h6' )
        host_h7 = self.addHost( 'h7' )
        host_h8 = self.addHost( 'h8' )

        switch_s1 = self.addSwitch( 's1' )
        switch_s2 = self.addSwitch( 's2' )
        switch_s3 = self.addSwitch( 's3' )
        switch_s4 = self.addSwitch( 's4' )
        switch_s5 = self.addSwitch( 's5' )
        switch_s6 = self.addSwitch( 's6' )
        switch_s7 = self.addSwitch( 's7' )
        
        self.addLink( host_h1, switch_s3 )
        self.addLink( host_h2, switch_s3 )
        
        self.addLink( host_h3, switch_s4 )
        self.addLink( host_h4, switch_s4 )
        
        self.addLink( host_h5, switch_s6 )
        self.addLink( host_h6, switch_s6 )
        
        self.addLink( host_h7, switch_s7 )
        self.addLink( host_h8, switch_s7 )
        
        self.addLink( switch_s3, switch_s2 )
        self.addLink( switch_s4, switch_s2 )
        
        self.addLink( switch_s6, switch_s5 )
        self.addLink( switch_s7, switch_s5 )
                
        self.addLink( switch_s2, switch_s1 )
        self.addLink( switch_s5, switch_s1 )

topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
