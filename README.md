osx-rdp-client
==============

```sh
# Summary:
{ seq 1 256 | while read i; do echo $i $(expr $i + 1000); done; } |
  while read oct local_oct; do
  echo python rdp.py --user Administrator --name $oct --ip 10.0.2.$oct --password mySecret;
  echo python rdp.py --user Administrator --name l$oct --ip localhost:$local_oct --password "mySecret"; done  >out
sh out >out2
sh out2 >out3
```

```sh
## Details
# outputs to out2:
python rdp.py --user Administrator --name 1 --ip 10.0.2.1 --password mySecret
python rdp.py --user Administrator --name l1 --ip localhost:1001 --password mySecret
python rdp.py --user Administrator --name 2 --ip 10.0.2.2 --password mySecret
python rdp.py --user Administrator --name l2 --ip localhost:1002 --password mySecret
python rdp.py --user Administrator --name 3 --ip 10.0.2.3 --password mySecret
python rdp.py --user Administrator --name l3 --ip localhost:1003 --password mySecret
```

```sh
# outputs to out2:
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarkorder.ids -array-add "'{f57221b3-951e-11e4-9cc6-7c6d628eb93d}'"
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.label -string "1"
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.hostname -string 10.0.2.1
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.username -string Administrator
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.fullscreen -string 0
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.resolution -string '@Size(1600 900)'
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57221b3-951e-11e4-9cc6-7c6d628eb93d}.password -string "mySecret"
sudo chown -R "demo:staff" /Users/demo/Library/Containers/com.microsoft.rdc.mac
sudo chmod -R 777 /Users/demo/Library/Containers/com.microsoft.rdc.mac
# sudo -u demo defaults read /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarkorder.ids -array-add "'{f57e590c-951e-11e4-a18e-7c6d628eb93d}'"
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.label -string "l1"
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.hostname -string localhost:1001
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.username -string Administrator
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.fullscreen -string 0
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.resolution -string '@Size(1600 900)'
defaults write /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist bookmarks.bookmark.{f57e590c-951e-11e4-a18e-7c6d628eb93d}.password -string "mySecret"
sudo chown -R "demo:staff" /Users/demo/Library/Containers/com.microsoft.rdc.mac
sudo chmod -R 777 /Users/demo/Library/Containers/com.microsoft.rdc.mac
# sudo -u demo defaults read /Users/demo/Library/Containers/com.microsoft.rdc.mac/Data/Library/Preferences/com.microsoft.rdc.mac.plist
```

```sh
sh out2
```
Updates com.microsoft.rdc.mac.plist
