from scapy.all import *
eth = Ether()
arp = ARP()
eth.dst="ff:ff:ff:ff:ff:ff"
#arp.pdst="10.10.10.0/24"

networkAddress = input("Enter the network address (example=10.10.10.0/24): ")
arp.pdst = networkAddress

#broadcast
bcPckt = eth/arp
#bcPckt.show()

#srp is like the sr but srp is layer2 packet
ans,unans= srp(bcPckt,timeout=5)
#ans.summary()
print("#"*30)
#unans.summary()

for snd,rcv in ans:
	#rcv.show()
	print(rcv.src, " ", rcv.psrc)
