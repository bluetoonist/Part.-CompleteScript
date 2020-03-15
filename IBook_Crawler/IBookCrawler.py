# -*- coding:utf8 -*-
"""
2019 01 20 : IBOOK Crawler

Note : Pycharm에서 csv 파일 생성시 파일제한이 걸려있는 듯 하다.

만약 백그라운드에서 동작하길 원한다면 headless 모드를 적용시키면 될 것

"""
# Need to Below Module
from bs4 import BeautifulSoup
from selenium import webdriver

import csv

# for save to open csv file
f = open('test.csv','w',encoding='euc-kr')
wr = csv.writer(f)

# Each PATH
path = "C:\\Users\\Owler\\PycharmProjects\\ALL_PROJECT\\chromedriver.exe"

# webdriver Setup
driver = webdriver.Chrome(path)

# URL Setting
url1 = 'http://www.ibookland.com/home/userguide/bookSearch.htm'

# Declare List Data Type
Subject = [] # Subject List

# List_Parsing_
driver.get(url1)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

SubjectList = soup.find('tr')
SubjectList2 = SubjectList.findAll('th',{'scope':'col'})

for item in SubjectList2:
    Subject.append(item.text)

print(Subject)
wr.writerow(Subject)

# scraping the tbody
BookINFO = soup.find("tbody").findAll('tr')

cnt = 0
for x in range(1,1412):
    for item, item2 in zip(BookINFO, range(0, len(BookINFO))):
        tmp = []

        Slciing = item.text.replace("\n", ' ').replace("\t", '')
        if item2 % 6 == 0:
            tmp.append(Slciing)
        else:
            tmp.append(Slciing)

        before = tmp[0].strip()

        after = before.split('  ')[2].replace(" ", ",") # for save to csvfile separaiton ','
        total = before.split('  ')[0] + ',' + before.split('  ')[1] + after # total data information

        wr.writerow(total.split(',')) # save to csv file
        del tmp  # temporary list delete

    # Execute NextPage
    driver.execute_script("goPage("+str(x+1)+")")

    # if Page Number = 10 then run Next List
    try:
        if x%10 == 0:
            driver.find_element_by_xpath('//*[@id="page-box"]/div/a[1]/span/img').send_keys('\n')
    except:
        continue

driver.close()
f.close()
