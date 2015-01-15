osx-rdp-client
==============

```sh
# Summary:
make >out
time sh -x out
```

out script looks like this:
```sh
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
