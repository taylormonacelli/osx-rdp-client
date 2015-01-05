#!/usr/bin/env python
# -*- python -*-

import uuid
from string import Template
import argparse
import os
import ConfigParser
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--user",help="rdp username")
parser.add_argument("-n", "--name",help="rdp connection name")
parser.add_argument("-i", "--ip",help="ip address")
parser.add_argument("-p", "--password",help="")

args = parser.parse_args()

loggedInUser=os.environ['USER']

RDCPLIST="/Users/%s/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist" %(loggedInUser)

s = Template("""
defaults write $RDCPLIST bookmarkorder.ids -array-add "'{$myUUID}'"
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.label -string "$connectionName"
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.hostname -string $host_ip
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.username -string $username
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.fullscreen -string 0
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.resolution -string '@Size(1600 900)'
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.password -string "$password"

# sudo chown -R "$loggedInUser:staff" /Users/$loggedInUser/Library/Containers/com.microsoft.rdc.mac
# sudo chmod -R 777 /Users/$loggedInUser/Library/Containers/com.microsoft.rdc.mac
# sudo -u $loggedInUser defaults read $RDCPLIST
""")

s1 = s.substitute(
    connectionName=args.name,
    RDCPLIST=RDCPLIST,
    myUUID=uuid.uuid1(),
    host_ip=args.ip,
    username=args.user,
    password=args.password,
    loggedInUser=loggedInUser,
    )

print s1
