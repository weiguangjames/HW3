Task 1: Defining custom topologies

Questions

1. What is the output of “nodes” and “net”
Nodes:
	available nodes are:
	c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7
net:
	h1 h1-eth0:s3-eth2
	h2 h2-eth0:s3-eth3
	h3 h3-eth0:s4-eth2
	h4 h4-eth0:s4-eth3
	h5 h5-eth0:s6-eth2
	h6 h6-eth0:s6-eth3
	h7 h7-eth0:s7-eth2
	h8 h8-eth0:s7-eth3
	s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
	s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
	s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
	s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
	s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
	s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
	s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
	c0

2. What is the output of “h7 ifconfig”
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
		inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
		inet6 fe80::5f7:9c9c:fe2f:53ef  prefixlen 64  scopeid 0x20<link>
		ether 8e:9c:4b:20:dc:b5  txqueuelen 1000  (Ethernet)
		RX packets 72  bytes 5476 (5.4 KB)
		RX errors 0  dropped 0  overruns 0  frame 0
		TX packets 12  bytes 936 (936.0 B)
		TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
		inet 127.0.0.1  netmask 255.0.0.0
		inet6 ::1  prefixlen 128  scopeid 0x10<host>
		loop  txqueuelen 1000  (Local Loopback)
		RX packets 0  bytes 0 (0.0 B)
		RX errors 0  dropped 0  overruns 0  frame 0
		TX packets 0  bytes 0 (0.0 B)
		TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


Task 2: Analyze the “of_tutorial’ controller

Questions
1. Draw the function call graph of this controller. For example, once a packet comes to thecontroller, which function is the first to be called, which one is the second, and so forth?
Then packet arrive to controller as below:

def _handle_PacketIn(self,event) -> sdef act_like_switch(self,packet, packet_in) -> def resend_packet(self,packet_in, out_port) -> self.connection.send(msg)

2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long does it take (on average) to ping for each case?
The average time of h1 ping h2 = 8.513ms
The average time of h1 ping h8 = 34.231ms

b. What is the minimum and maximum ping you have observed?
h1 ping h2:
	min: 1.24ms
	max: 19.761ms
h1 ping h8:
	min: 5.07ms
	max: 62.391ms

c. What is the difference, and why?

H1 ping h8 takes much more time than h1 ping h2, because the packets between h1 and h8 have to travel through multiple switches than h1 and h2.

3. Run “iperf h1 h2” and “iperf h1 h8”
a. What is “iperf” used for?

It is used to test TCP bandwidth to evaluate the network performance and quality of the network line.

b. What is the throughput for each case?
h1-> h2: 
Results: [‘10.44 Mbits/sec’,’12.03 Mbits/sec’]
h1-> h8: 
Results: [‘9.71 Mbits/sec’,’47.26 Mbits/sec’]

c. What is the difference and explain the reasons for the difference.
H1 ping H8 is longer compared to H1 ping H2, because the greater number of switches between H1 & H8

4. Which of the switches observe traffic? Please describe your way for observing 
Output each switch. Accourding to binary tree topology created, we can see for "iperf H1 H2", s3 observes traffic & for "iperf H1 H8", s3, s2, s1, s5, s7 observe traffic.


Task 3: MAC Learning Controller
Questions
1. Describe how the above code works, such as how the "MAC to Port" map is established. You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).
Enable the "act_like_switch" function, there is learning by mapping of each switch connection to host.
When the source Mac isn't in the map mac_to_port, script adds add the {Mac, Port} into map mac_to_port
if the destination MAC is the map, script sends the packet out the port associated with the MAC.
When the destination MAC isn't in the map, script sends output to all ports except the input port.

2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long did it take (on average) to ping for each case?
The average time of h1 ping h2 = 4.362 ms
The average time of h1 ping h8 = 22.474ms

b. What is the minimum and maximum ping you have observed?
h1 ping h2:
	min: 1.641 ms
	max: 5.299 ms
h1 ping h8:
	min: 6.782 ms
	max: 38.563 ms

c. Any difference from Task 2 and why do you think there is a change if there is?
 Task 3 average result is better than Task 2 average result. This is beacuse of "mac_to_port" is established. There is no flooding of packets everywhere.

3. Run “iperf h1 h2” and “iperf h1 h8”.
a. What is the throughput for each case?
Iperf h1 h2:
	Results: [’45.1 Mbits/sec’, ’49.7 Mbits/sec’]
Iperf h1 h8:
	Results: [’7.34 Mbits/sec’, ’8.16 Mbits/sec’]

b. What is the difference from Task 2 and why do you think there is a change if there is?
Yes, the different in throughput for "iperf H1 H2". It has increased in case of Task3. After the "mac_to_port" established there is no flooding of packets everywhere. 
