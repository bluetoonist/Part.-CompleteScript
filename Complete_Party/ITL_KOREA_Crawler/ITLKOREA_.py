#-*- coding:utf-8 -*-
import ssl
import urllib.request
import urllib3
from bs4 import BeautifulSoup

# Setting SSL Certificate Error
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()
context = ssl._create_unverified_context()

# ITL Tech URL
ItlURL = "https://www.itlkorea.kr/technote/"

# URL Access
req = urllib.request.Request(ItlURL)
reopen = urllib.request.urlopen(req,context=context)

# Hangule Boken Setup
htmlpasre = reopen.read().decode('cp949')

# Html Parsing
parse= BeautifulSoup(htmlpasre,"html.parser")

# table tag
element = parse.find_all("span",{"class":"txt_blue"})

# Document Download Logic
for item in element:
    Link_addr = item.find("a").get("href")
    AticleName = item.text.strip()

    if "view.html" in Link_addr:
        Number = Link_addr[20::].replace("N","n")
        DownloadURL = "https://www.itlkorea.kr/technote/download.php?"+Number+"&atNo=1"
        urllib.request.urlretrieve(DownloadURL,"C:\\Users\\Jan\\Desktop\\Document\\"+AticleName+'.pdf')
    else:
        pass

