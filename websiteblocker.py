host_path = "C:\Windows\System32\ drivers\etc\hosts"
redirect = "https://learn.epam.com/myLearning/program?groupGuid=0480eec1-0a05-40c0-b714-1add69d5e63d&tab=calendar"
websitelist = ["https://www.youtube.com/","https://www.tut.by/","https://www.instagram.com/"]

import time
from datetime import datetime as dt

while True:
    ymd =(dt.now().year,dt.now().month,dt.now().day)
    if dt(*ymd,8) < dt.now()< dt(*ymd,16):
        print("It's time to work")
        file = open(host_path, "r+")
        content = file.read()
        for website in websitelist:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    else:
        print("You can have a rest")
    time.sleep(5)

