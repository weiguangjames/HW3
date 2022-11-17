
import pox.openflow.libopenflow_01 as of\

log = core.getLogger()

class Tutorial (object):
  """
  A Tutorial object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
def __init__ (self, connection):

    self.connection = connection

    connection.addListeners(self)
    self.mac_to_port = {}

def resend_packet (self, packet_in, out_port):
    """
    Instructs the switch to resend a packet that it had sent to us.
    "packet_in" is the ofp_packet_in object the switch had sent to the controller due to a table-miss.
    """
    msg = of.ofp_packet_out()

    msg.data = packet_in
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    self.connection.send(msg)

def act_like_hub (self, packet, packet_in):
    """
    Implement hub-like behavior -- send all packets to all ports besides
    the input port.
    """

    self.resend_packet(packet_in, of.OFPP_ALL)

def act_like_switch (self, packet, packet_in):
     if packet.src not in self.mac_to_port:
        self.mac_to_port[packet.src] = packet_in.in_port
     if packet.dst in self.mac_to_port:
        
        self.resend_packet(packet_in, self.mac_to_port[packet.dst])
     else:
        self.resend_packet(packet_in, of.OFPP_ALL)

def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed 
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp
    print("Swtich:", event.connection,"source address :", packet.src,"destination address:", packet.dst)
    
    self.act_like_switch(packet, packet_in)

def launch ():
  """
  Starts the component
  """
def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Tutorial(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
}
