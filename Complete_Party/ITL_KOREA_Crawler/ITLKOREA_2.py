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
for x in range(3400,4000):
    ret = "no="+str(x)

    DownloadURL = "https://www.itlkorea.kr/technote/download.php?" + ret + "&atNo=1"
    print(DownloadURL)
    urllib.request.urlretrieve(DownloadURL,"C:\\Users\\Jan\\Desktop\\Document\\"+str(x)+".pdf")
