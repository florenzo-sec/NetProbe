import socket
from args import parse_ports,args

for p in parse_ports(args()):
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket generation
    s.settimeout(2) # timeout so the scanner doesn't wait infinitly
    
    if s.connect_ex((args()["host"],p))!=0: #port is open=0, else >0
        print("Porta chiusa")
    else:
        print("Porta aperta")
        
            