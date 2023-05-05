import time
from datetime import datetime as dt
import os 

# hosts path name 
hosts_path = "/etc/hosts"

# Write Website Hosts Names 
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

# Ip Address 
redirect = "127.0.0.1"

# Blocking Hours 
start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8) # 8am
end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16) # 4pm

def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                # add the website to the hosts file of that perticular Ip Address 
                file.write(redirect + " " + website + "\n")
# Working Hours 
def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

while True:
    # check if the current time is within the blocking period
    if start_time < dt.now() < end_time:
        block_websites()
    else:
        unblock_websites()
    time.sleep(5)
