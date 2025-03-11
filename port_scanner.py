import socket
import ipaddress
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    ip_address = None
    host_name = None

    try:
        ip_address = socket.gethostbyname(target)        
        host_name = target
    except ValueError:
        try:
            ip_address = socket.gethostbyname(target)
            host_name = target 
        except socket.gaierror:
            return "Error:Invalid hostname"
    if not ip_address:
        return "Error:Invalid IP address"  

    for port in range(port_range[0],port_range[1]+i):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip_address,port))
            if result == 0:
                open_ports.append(port)  
    if not verbose:
        return open_ports

    result = f"Open ports for (host_name)({ip_address})\nPORT      SERVICE"

    for port in open_ports:
        service_name = ports_and_services.get(port, "unknown")
        result += f"\n{port:<9}{service_name}"




    return(open_ports)