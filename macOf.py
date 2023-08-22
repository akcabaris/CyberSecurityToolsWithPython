from scapy.all import *
#creating random packets(in here 10) and add them to the pckt_list and send 
pckt_list =[]
for i in range(10):
	srcMac = RandMAC()
	dstMac = RandMAC()
	srcIp = RandIP()
	dstIp = RandIP()

	ether = Ether(src=srcMac,dst=dstMac)
	ip = IP(src=srcIp,dst=dstIp)
	pckt = ether/ip
	pckt_list.append(pckt)
	print(srcMac," : ",srcIp,">>>>",dstMac," : ",dstIp)
#layer2
sendp(pckt_list,iface="eth0",verbose=False)