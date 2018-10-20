import time
import os
from datetime import datetime as dt

if os.name == 'posix':
    hosts_file=("/private/etc/hosts") # on an ubuntu platform it can be found here
    # hosts_file=("hostslist") # for testing purposes
elif os.name == 'nt':
    hosts_file=r"C:\Windows\System32\Drivers\etc\hosts"



local="127.0.0.1"
website_list=[] # empty is better



stime = dt.now().hour
k = 1
etime = stime + k

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

def remover(value):  # added for instant removal of site from the list
    with open(hosts_file,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if value not in line:
                file.write(line)
        file.truncate()
