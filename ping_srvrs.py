import os
import sys


AX = "10.11.100.100"
xerp = "10.0.71.11"
NAS = "10.0.71.16"
CDSGAX = "103.101.16.250"
Servers = [AX, xerp, NAS, CDSGAX]
cmd = "ping " 
#VPN = "10.10.23.250"
while True:
    print("")
    choice = str(input("Choose server that you want to send ICMP packet: "))
    print("")
    if choice == "h":
        print("""                 1 = AX   
                 2 = Xerp
                 3 = NAS
                 4 = Jumpserver""") 
    elif choice == "1":
        os.system(cmd + AX) 
    elif choice == "2":
        os.system(cmd + xerp)
    elif choice == "3":
        os.system(cmd + NAS)
    elif choice == "4":
        os.system(cmd + CDSGAX)
    elif choice == "a":
        for i in Servers:
            print("")
            print("=============== [ " + i + " ] ===============")
            os.system(cmd + i) 
    elif choice == "exit" and "quit":
       break
    else:
        os.system(cmd + choice)
    
