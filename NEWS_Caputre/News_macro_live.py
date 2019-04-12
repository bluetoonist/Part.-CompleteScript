
from selenium import webdriver
from selenium.webdriver.common.by import  By
import requests
from bs4 import BeautifulSoup
from time import sleep
import time
import os

# Site : www.daum.net

## keyword_input = str(input("검색할 KeyWord : "))

keyword_input = str(input(" KEYWORD : "))
key_str = ""
l1 = []

r = requests.get("http://search.daum.net/search?w=tot&DA=23A&rtmaxcoll=NNS&q=" + keyword_input)
c = r.content
soup = BeautifulSoup(c, "html.parser")

dn = soup.find("div", {"class": "wrap_gnb"})
dn2 = dn.find("ul", {"class": "gnb_search"})
dn3 = dn2.findAll("a")

for item in dn3:
    l1.append(item.get("href"))

# 다음 사이트의 뉴스 목록을 keyword로 검색한 결과를 저장
l1 = "search" + l1[1]

# 최신 순위 정렬 URL를 가져오는 태그
r = requests.get("http://search.daum.net/" + l1)
c = r.content
soup = BeautifulSoup(c, "html.parser")

dsort_ = soup.find("div", {"class": "sort_comm"})
dsort_1 = dsort_.findAll("a")

for item in dsort_1:
    key_str = item.get("href")

driver_path = str(input(" ON THE CHROME DRIVER : "))
site_link = []

cnt = 1
cur_title = ""
while True:
    r = requests.get("http://search.daum.net/search" + key_str)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    r = requests.get("http://search.daum.net/search" + key_str)
    c = r.content
    soup1 = BeautifulSoup(c, "html.parser")

    link_1 = soup1.find("div", {"class": "coll_cont"})
    link_2 = link_1.find("ul", {"id": "newsResultUL"})
    link_3 = link_2.find("div", {"class": "wrap_cont"})
    link_4 = link_3.find("div", {"class": "cont_inner"})

    link_ = link_4.find("div", {"class": "wrap_tit mg_tit"}).find("a").get("href")  # 기사 링크
    title = link_4.find("div", {"class": "wrap_tit mg_tit"}).text.replace("\n", '')  # 기사 제목
    content = link_4.find("p", {"class": "f_eb desc"}).text  # 기사 내용
    date_time = link_3.find("span", {"class": "f_nb date"}).text.split("\n")[1]  # 기사 뜬 시간

    try:
        if cur_title != title:
            cur_title = title
            print(cur_title, " ", time.gmtime().tm_hour + 9, "시", time.gmtime().tm_min, "분", '\n')
            print("기사 내용 :", content)
            print(" 새 기사는 파일을 실행한 경로에 저장됩니다")

            dt = str(time.localtime().tm_hour) + "시" + str(time.localtime().tm_min) + "분"

            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1440x2560')
            options.add_argument('disable-gpu')
            driver = webdriver.Chrome(driver_path, chrome_options=options)

            driver.get(link_)
            driver.implicitly_wait(10)
            driver.save_screenshot("./www_daum_net 캡쳐 기사" + str(int(cnt)) + "번 쨰" + dt + ".png")
            cnt += 1
            sleep(15)
            driver.close()
            os.system("cls")
        else:
            print("갱신 중...")
            sleep(10)
            os.system("cls")
    except:
        pass






