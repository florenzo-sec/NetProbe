import socket
from args import parse_ports,args
import colorama
from concurrent.futures import ThreadPoolExecutor

colorama.init(autoreset=True) #set terminal colors autoreset

def port_scan(host,p):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket generation
    s.settimeout(2) # timeout so the scanner doesn't wait infinitly

    status = s.connect_ex((host,p))

    if status!=0: #port is open=0, else >0
        print(f"[{colorama.Fore.RED}CLOSED{colorama.Fore.RESET}]\t{p}")
    else:
        print(f"[{colorama.Fore.GREEN}OPEN{colorama.Fore.RESET}]\t{p}")
    
    s.close()

arguments = args() # grab arguments from CLI

print(f"Scanning {arguments['host']} using {arguments['threads']} threads.")

with ThreadPoolExecutor(max_workers=arguments['threads']) as executor:
    futures = [executor.submit(port_scan,arguments['host'],p) for p in parse_ports(arguments)]
    for future in futures:
        future.result()
            
