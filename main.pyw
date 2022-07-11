#This pro

import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # path to hosts file
redirect="127.0.0.1"
website_list=open(r"block_list.txt").read().splitlines()    # list of site to block

print("Enter time interval when you want block the websites, 2 numbers: ")
start=int(input())
end=int(input())

while True:
    #comparing current date and time with my working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end):
        print("-Working hours...\nSome websites are blocked.-\n")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("-Not Working hours.\nYou are free to visit all websites.-\n")
        with open(hosts_path,'r') as file:
            content=file.readlines()
        with open(hosts_path,'w') as file:
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

    time.sleep(5)