import time
import os
from datetime import datetime as dt

#class OS(Enum):
#    def checkPlatform(osName):
#        return osName.lower()== platform.system().lower()
#
#    MAC = checkPlatform("darwin")
#    LINUX = checkPlatform("linux")
#    WINDOWS = checkPlatform("windows")
#
#if OS.MAC or OS.LINUX:
if os.name == 'mac':
    hosts_file=("/private/etc/hosts")
elif os.name == 'nt':
    hosts_file=r"C:\Windows\System32\Drivers\etc\hosts"

#elif OS.WINDOWS:
#    hosts_file=r"C:\Windows\System32\Drivers\etc\hosts"



local="127.0.0.1"
website_list=["www.facebook.com"]

stime=9
etime=17

def start():
 global website_list
 global stime
 global etime
 while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,stime) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,etime):
        with open(hosts_file,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(local+" "+ website+"\n")
    else:
        with open(hosts_file,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    break
    time.sleep(720)



