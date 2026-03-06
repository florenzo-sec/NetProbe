import socket
from args import parse_ports,args
import colorama
import threading

colorama.init(autoreset=True) #set terminal colors autoreset

def port_scan(host,p):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket generation
    s.settimeout(2) # timeout so the scanner doesn't wait infinitly

    status = s.connect_ex((arguments["host"],p))

    if status!=0: #port is open=0, else >0
        print(f"[{colorama.Fore.RED}CLOSED{colorama.Fore.RESET}]\t{p}")
    else:
        print(f"[{colorama.Fore.GREEN}OPEN{colorama.Fore.RESET}]\t{p}")
    
    s.close()

arguments = args() # grab arguments from CLI

print(f"Scanning {arguments['host']}\n")

threads = []

for p in parse_ports(arguments):
    t = threading.Thread(target=port_scan,args=(arguments['host'],p))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
            
