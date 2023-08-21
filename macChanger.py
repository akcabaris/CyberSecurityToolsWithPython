import random
import subprocess
import re

charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

a = random.choice(charList)
newMac=""
for i in range(12):
	newMac=newMac+random.choice(charList)
print(newMac)

ifconfigResult = subprocess.check_output("ifconfig eth0",shell=True).decode()
#print(ifconfigResult)

#full
#oldMac = re.search("ether (.+) ",ifconfigResult).group().split(" ")

#just the mac address in the group
#oldMac = re.search("ether (.+) ",ifconfigResult).group().split(" ")[1]
#choose any of this two
oldMac = re.search("ether (.*?)txqueuelen",ifconfigResult).group(1).strip()
print("Old MAC: ", oldMac)
print("New Mac: ", newMac)

subprocess.check_output("ifconfig eth0 down",shell=True)
subprocess.check_output("ifconfig eth0 hw ether "+newMac,shell=True)  
subprocess.check_output("ifconfig eth0 up",shell=True)