import os
import uuid
from string import Template

class RDP:

    loggedInUser = os.environ['USER']

    RDCPLIST="/Users/%s/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist" %(loggedInUser)

    def __init__(self,label,host,username,password):
        self.label = label
        self.host = host
        self.username = username
        self.password = password
        self.fullscreen = 0
        self.resolution = '@Size(1600 900)'
        self.uuid = uuid.uuid1()
        self.loggedInUser = RDP.loggedInUser

    def display(self):
        s = Template("""
defaults write $RDCPLIST bookmarkorder.ids -array-add "'{$myUUID}'"
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.label -string "$connectionName"
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.hostname -string $host_ip
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.username -string $username
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.fullscreen -string 0
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.resolution -string '@Size(1280 720)'
defaults write $RDCPLIST bookmarks.bookmark.{$myUUID}.password -string "$password"

# sudo chown -R "$loggedInUser:staff" /Users/$loggedInUser/Library/Containers/com.microsoft.rdc.mac
# sudo chmod -R 777 /Users/$loggedInUser/Library/Containers/com.microsoft.rdc.mac
# sudo -u $loggedInUser defaults read $RDCPLIST
""")
        s1 = s.substitute(
            connectionName = self.label,
            RDCPLIST = RDP.RDCPLIST,
            myUUID = self.uuid,
            host_ip = self.host,
            username = self.username,
            password = self.password,
            loggedInUser = self.loggedInUser
        )

        return s1
