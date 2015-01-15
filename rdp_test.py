#!/usr/bin/env python

import RDP
import ipcalc
import re

name_prefix="o"

for ip in ipcalc.Network('10.0.2.0/24'):
    octet = re.search( r'(\d+)$', str(ip)).group(1)
    name = "%s%s" % (name_prefix,octet)
    r = RDP.RDP(name,ip,'Administrator','Stre@mb0x')
    print r.display()

name_prefix="n"

for ip in ipcalc.Network('10.0.3.0/24'):
    octet = re.search( r'(\d+)$', str(ip)).group(1)
    name = "%s%s" % (name_prefix,octet)
    r = RDP.RDP(name,ip,'Administrator','Stre@mb0x')
    print r.display()


# Create connection lo125 to connect to localhost:1125 for example

name_prefix="lo"

for ip in ipcalc.Network('10.0.2.0/24'):
    octet = re.search( r'(\d+)$', str(ip)).group(1)
    name = "%s%s" % (name_prefix,octet)
    om = int(str(octet)) + 2000 # 2000 for 10.0.2.0
    ip = 'localhost:%s' % om
    r = RDP.RDP(name,ip,'Administrator','Stre@mb0x')
    print r.display()

name_prefix="ln"

for ip in ipcalc.Network('10.0.3.0/24'):
    octet = re.search( r'(\d+)$', str(ip)).group(1)
    name = "%s%s" % (name_prefix,octet)
    om = int(str(octet)) + 3000 # 3000 for 10.0.3.0
    ip = 'localhost:%s' % om
    r = RDP.RDP(name,ip,'Administrator','Stre@mb0x')
    print r.display()
