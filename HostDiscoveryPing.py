from scapy.all import *

ip = IP()
icmp = ICMP()
pingPckt = ip/icmp
addr = "10.10.10."
ipList = []

for i in range(50):
	pingPckt[IP].dst=addr+str(i)
	#print(pingPckt[IP].dst)
	response = sr1(pingPckt,timeout=0.5,verbose=False)
	#print(response)
	if(response):
		#print(pingPckt[IP].dst, "is up")
		#append used for add to list
		ipList.append(pingPckt[IP].dst)
	else:
		pass
print(ipList)