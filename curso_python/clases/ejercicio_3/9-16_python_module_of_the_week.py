"""
9-16. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
https://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, perhaps starting with the random
module.
"""
import ipaddress
from socket import gethostname
print(gethostname())

NETWORKS = [
'192.168.10.0/27',
'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print(' is private:', net.is_private)
    print(' broadcast:', net.broadcast_address)
    print(' compressed:', net.compressed)
    print(' with netmask:', net.with_netmask)
    print(' with hostmask:', net.with_hostmask)
    print(' num addresses:', net.num_addresses)
    print()