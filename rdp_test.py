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
