import os
import wmi
import psutil
import sqlite3

for p in psutil.process_iter():
    if "chrome.exe" in p.name():
        os.system("taskkill /f /im chrome.exe")
    else:
        continue

save_data_dir = os.getcwd()
path = os.getenv("APPDATA")
os.chdir(path)
os.chdir('../')
os.chdir('.//Local//Google//Chrome//User Data//Default')

conn = sqlite3.connect("History")
cur = conn.cursor()

sql = "SELECT url,title,visit_count,datetime( (last_visit_time/1000000)-11644473600, 'unixepoch' ,'localtime') as time from urls"
cur.execute(sql)
rows = cur.fetchall()

os.chdir(save_data_dir)
with open("./getLog.txt","wt",encoding="utf8") as f:
    for row in rows:
        parsing = "".join(str(row))
        parsing += "\n"
        f.write(parsing)
conn.close()