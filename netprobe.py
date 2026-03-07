import socket
from args import parse_ports,args
from concurrent.futures import ThreadPoolExecutor
import time

stats = {} # dict containing all of the port stats(open or closed)

def port_scan(host,p):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket generation
    s.settimeout(2) # timeout so the scanner doesn't wait infinitly

    status = s.connect_ex((host,p))

    if status!=0: #port is open=0, else >0
        stats[p] = "CLOSE"
    else:
        stats[p] = "OPEN"
    
    s.close()

def output(stats):
    for p in stats:
        if stats[p]=="OPEN":
            print(f"{p} [OPEN]")
        else:
            print(f"{p} [CLOSED]")

arguments = args() # grab arguments from CLI

print(f"Scanning {arguments['host']} using {arguments['threads']} threads.")

start = time.time() #start timer

with ThreadPoolExecutor(max_workers=arguments['threads']) as executor: 
    futures = [executor.submit(port_scan,arguments['host'],p) for p in parse_ports(arguments)] # workers generator
    for future in futures:
        future.result()

output(stats)
            
end = time.time()-start


print(f"Scan completed in {round(end,2)} seconds, {sum(1 for value in stats.values() if value=="OPEN")} open ports.")
