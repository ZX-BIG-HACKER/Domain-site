import socket
from os import system
from time import sleep
import time
import os
import socket
import random
import threading
import logging
import sys
import urllib
import _thread
class colorma:


    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print("")
print("           please wait....")
time.sleep(0.5)
os.system("pip install socket")
os.system("apt install screenfetch -y")
os.system("clear")
os.system("screenfetch")
time.sleep(2)
os.system("clear")

try: system("clear")
except: system ("class")
s = "\033[91m\033"
print (s+" 0% [=                              ]")
sleep (0.3)
try: system("clear")
except: system ("class")
print ("15% [===                         ]")
sleep (0.3)
try: system ("clear")
except: system("class")
print ("20% [=======                      ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("30% [=========                 ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("45% [==============          ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("65% [=======================          ]")
sleep (0.3)
try: system ("clear")
except: system("class")
print ("85% [=============================       ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("100% [========================================================]")
sleep (1)
os.system("clear")

print(f"""{colorma.GREEN}
  ▒▒███▒▒▒▒███                                     ▒▒▒
   ▒███   ▒▒███  ██████  █████████████    ██████   ████  ████████
   ▒███    ▒███ ███▒▒███▒▒███▒▒███▒▒███  ▒▒▒▒▒███ ▒▒███ ▒▒███▒▒███
   ▒███    ▒███▒███ ▒███ ▒███ ▒███ ▒███   ███████  ▒███  ▒███ ▒███
   ▒███    ███ ▒███ ▒███ ▒███ ▒███ ▒███  ███▒▒███  ▒███  ▒███ ▒███
   ██████████  ▒▒██████  █████▒███ █████▒▒████████ █████ ████ █████
  ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒


""")

print(f"\n{colorma.YELLOW}___________________________________________________________________________")

print(f"\n{colorma.CYAN}            github link : https://github.com/ZX-BIG-HACKER                                  ")
print("                       Script builder : ZX HACK                     ")
print(f"\n{colorma.YELLOW}___________________________________________________________________________")
domain = input(f"{colorma.RED}Target Domain »: ").lower()

domain = domain.replace("http://","")
domain = domain.replace("https://","")
domain = domain.replace("www.","")

if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server =  "whois.iana.org"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((whois_server,43))

s.send((domain+"\r\n").encode())

msg = s.recv(10000)

print(msg.decode())

print(f"\n{colorma.YELLOW}___________________________________________________________________________")