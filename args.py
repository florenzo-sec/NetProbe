import argparse

def args():
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument('host',help='The host you want to scan')
    parser.add_argument('-p','--port',help='Ports to scan (comma-separated or range: 22,80 or 22-443)', required=True)
    return vars(parser.parse_args())

def parse_ports(ports_arg):
    
    ports = []
    
    ports_args_list = ports_arg["port"].split(",") #turn arg into a list, separating when "," is found
    
    for i in ports_args_list:
        if "-" in i: #range case
            start,end = i.split("-")
            ports.extend(range(int(start),int(end)+1))
        else:
            ports.append(int(i)) #normal case

    return ports

