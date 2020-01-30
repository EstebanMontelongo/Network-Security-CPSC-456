import nmap        
import paramiko
import netinfo     # sudo pip install pynetinfo

portScanner = nmap.PortScanner()
portScanner.scan('192.168.1.0/24')

print(portScanner.all_hosts())
