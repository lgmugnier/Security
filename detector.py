#Lucie Mugnier
#U87775286

import dpkt
import socket

f = open("lbl-internal.20041004-1305.port002.dump.anon", "rb")
pcap = dpkt.pcap.Reader(f)
syn = []
synack = []

for ts, buf in pcap:
	try:
		eth = dpkt.ethernet.Ethernet(buf)
		if eth.type == dpkt.ethernet.ETH_TYPE_IP:
			ip = eth.data
			if ip.p == dpkt.ip.IP_PROTO_TCP:
				tcp = ip.data
				if tcp.flags == 2:
					src = socket.inet_ntoa(ip.src)
					syn.append(src)
				if tcp.flags == 18:
					dst = socket.inet_ntoa(ip.dst)
					synack.append(dst)
	except dpkt.dpkt.UnpackError:
		continue
		
print "check starting..." 

while len(syn) > 0:
	addr = syn[0]
	if syn.count(addr) >= synack.count(addr) * 3:
		print addr
	syn = [v for v in syn if v != addr]

f.close()