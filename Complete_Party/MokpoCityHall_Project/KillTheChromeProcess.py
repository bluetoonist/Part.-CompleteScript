#-*- coding:utf8 -*-

# ChromeProcess Quit
# Kill the Zombie chromedriver process

import wmi
import os

c = wmi.WMI()

for process in c.win32_process():
   # print(process.ProcessID ,process.Name)

    if process.Name == "chromedriver.exe":
        os.system("taskkill /f /im "+process.Name)
    else:
        continue
