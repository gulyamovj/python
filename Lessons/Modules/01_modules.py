# Task
import ipaddress
def has_access(ip, network):
    ip_addr = ipaddress.ip_address(ip)
    net = ipaddress.ip_network(network)

    return ip_addr in net.hosts()

access = has_access("91.142.84.30", "91.142.84.0/27")
print(access)  # True