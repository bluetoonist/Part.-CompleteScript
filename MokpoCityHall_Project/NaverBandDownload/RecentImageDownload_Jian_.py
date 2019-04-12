# 2018.11.25~ 2019.1.25 에서 있었던 목포시 일자리 사업
# 업무자동화 Script 증

# Naver Band Image Download script
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

import time
import os
import shutil

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Your Chrome Driver Path
chrome_driver = ""
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.find_element_by_xpath('//*[@id="content"]/section/div[9]/div/div[1]/div/div[2]/div/button').send_keys('\n')
time.sleep(1.5)

# Recent Post URL IDX NUMBER
RecentPosting = driver.page_source
soup = BeautifulSoup(RecentPosting, "html.parser")

FirstRecentPost = soup.find("ul", {"class": "_postMoreMenuUl"})
FirstRecentPost2 = FirstRecentPost.find("li")
FirstRecentPost3 = FirstRecentPost2.find("a")

Parsing = str(FirstRecentPost3)

MostRecentPosting = Parsing.split('=')[2].split('"')[1]
ExtractionRecetPosting = MostRecentPosting.split('/')

# URL 주소 파싱
BaseINDEX = "https://band.us/band/73394308/post/"
LastIndex = ExtractionRecetPosting[-1]

count = -1
print(BaseINDEX + LastIndex)

# Total URL Path
DownloadPath = 'C:\\Users\\MokpoBIZ\\Desktop\\Working\\Working2\\Recenting_Posting'
DownloadDIR = "C:\\Users\\MokpoBIZ\\Downloads"

# Name LIST
Namelist = []

IndexRUN2 = int()

# Recent Download Start
from time import sleep

while True:
    # Start Reverse
    counting = (int(LastIndex)+1) + count

    # counting = 3664 + count
    print("============================================")
    print('Counting Here', counting)
    count -= 1
    soup = ""
    time.sleep(1.5)

    # Recent Break Point
    if counting == 3684:
        exit(1)
    else:
        pass

    try:
        time.sleep(2)
        driver.get(BaseINDEX + str(counting))
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

    except:
        Alert(driver).accept()
        continue
    time.sleep(1)
    # 정보
    SearchINFO = soup.find("div", {"data-viewname": "DPostAuthorView"})
    SearchINFO2 = SearchINFO.find("div", {"class": "postWriterInfoWrap"})

    # 이름찾기
    Name = SearchINFO2.find("strong").text
    SearchTIME = SearchINFO2.find("time", {"class": "time"}).text
    timeline = SearchTIME.replace(":", "_")
    # 상가정보가 있는가?
    StoreName = soup.find("div", {"data-viewname": "DPostContentListView"}).text
    StoreName = StoreName.strip()

    print(Name + ' ' + SearchTIME + ' ' + StoreName)
    New_FOLDER_Name = Name + ' ' + timeline + ' ' + StoreName

    time.sleep(1)

    for rd in Namelist:
        if rd in Name:
            print("[+]RunCode")

            try:
                SearchClipText = soup.find("div", {"data-viewname": "DPostTextView"}).text
                New_FOLDER_Name = Name + '' + SearchClipText + '' + timeline
                print("Search clip text : ", SearchClipText)
                driver.find_element_by_xpath('//*[@id="content"]/div/section/div/div/div[3]/div[3]/div[2]').click()

            except NoSuchElementException:
                continue

            except AttributeError:
                # 상가를 적지 않은 상호명
                SearchClipText = "상호명없음"

                print(Name + '' + SearchClipText + '' + timeline)

                New_FOLDER_Name = Name + '' + SearchClipText + '' + timeline
                print(New_FOLDER_Name)
                driver.find_element_by_xpath('//*[@id="content"]/div/section/div/div/div[3]/div[3]/div[1]').click()
                time.sleep(1)

                PostForm = driver.page_source
                soup = BeautifulSoup(PostForm, "html.parser")

                # 게시글의 마지막 번호만큼 for문을 돌리기 위해 추출함
                PageLastIndex = soup.find("div", {"class": "pageView"})
                # 게시글의 마지막 번호가 담긴 Variable
                PageLastIndex2 = PageLastIndex.find("span").text

                for x in range(1, int(PageLastIndex2) + 1):
                    if x == 1:
                        time.sleep(0.5)
                        DownloadHTML = driver.page_source
                        soup = BeautifulSoup(DownloadHTML, "html.parser")
                        DownloadLingGet = soup.find("div", {"class": "optionBox"})
                        DownloadLingGet2 = DownloadLingGet.find("a").get("href")
                        driver.get(DownloadLingGet2)
                        time.sleep(0.5)
                        driver.find_element_by_xpath(
                            '//*[@id="wrap"]/div[2]/div/div/section/div/div[1]/span/button').send_keys('\n')
                    else:
                        try:
                            time.sleep(0.5)
                            DownloadHTML = driver.page_source
                            soup = BeautifulSoup(DownloadHTML, "html.parser")
                            DownloadLingGet = soup.find("div", {"class": "optionBox"})
                            DownloadLingGet2 = DownloadLingGet.find("a").get("href")
                            driver.get(DownloadLingGet2)
                            time.sleep(0.5)
                            driver.find_element_by_xpath(
                                '//*[@id="wrap"]/div[2]/div/div/section/div/div[1]/span[2]/button').send_keys('\n')
                        except:
                            # Total URL Path

                            # DirectoryName = " "
                            print("FOLDERNAMEHERE", New_FOLDER_Name)

                            os.chdir(DownloadPath)  # 현재 작업 디렉토리 변경
                            print(os.getcwd())
                            os.makedirs(New_FOLDER_Name)

                            time.sleep(1)

                            try:
                                cnt = 0
                                for rd in os.listdir(DownloadDIR):
                                    if ".jpg" in rd:
                                        cnt += 1
                                        shutil.move(DownloadDIR + "/" + rd, DownloadPath + "/" + New_FOLDER_Name)
                                print("Total IMAGE : ", cnt)
                            except:
                                break
                continue

            time.sleep(1.5)
            print("="*20 +"절취선"+"="*20)
            print(SearchClipText)

            DownloadHTML2 = driver.page_source
            soup2 = BeautifulSoup(DownloadHTML2, "html.parser")
            # 상가를 적어놓은 게시글의 다운로드 페이지 인덱스

            LinkGetStorePageView = soup2.find("div", {"class": "pageView"})
            LinkGetStorePageView2_MAX = LinkGetStorePageView.find("span").text
            LinkGetStorePageView2_MIN = LinkGetStorePageView.find("strong").text

            print(" MIN :",LinkGetStorePageView2_MIN, "MAX :",LinkGetStorePageView2_MAX)

            if int(LinkGetStorePageView2_MIN) == 1:  # 상가명이 '위'에 적혀있을시 1부터 시작
                for x in range(1, int(LinkGetStorePageView2_MAX) + 1):
                    if x == 1:
                        Html = driver.page_source
                        soup = BeautifulSoup(Html, "html.parser")
                        DownloadLinkGetStore1 = soup.find("div", {"class": "optionBox"})
                        DownloadLinkGetStore2 = DownloadLinkGetStore1.find("a").get("href")
                        # print("상가명이 위에")
                        driver.get(DownloadLinkGetStore2)
                        time.sleep(0.5)
                        driver.find_element_by_xpath(
                            '//*[@id="wrap"]/div[2]/div/div/section/div/div[1]/span/button').send_keys('\n')
                    else:
                        try:
                            time.sleep(1)
                            Html = driver.page_source
                            soup = BeautifulSoup(Html, "html.parser")
                            DownloadLinkGetStore1 = soup.find("div", {"class": "optionBox"})
                            DownloadLinkGetStore2 = DownloadLinkGetStore1.find("a").get("href")
                            driver.get(DownloadLinkGetStore2)
                            driver.find_element_by_xpath(
                                '//*[@id="wrap"]/div[2]/div/div/section/div/div[1]/span[2]/button').send_keys('\n')
                        except:
                            # Total URL Path
                            # DirectoryName = " "
                            print("Folder Name Here :",New_FOLDER_Name)

                            os.chdir(DownloadPath)  # 현재 작업 디렉토리 변경
                            print('[+]Created : ',os.getcwd())
                            os.makedirs(New_FOLDER_Name)

                            time.sleep(1.5)

                            try:
                                cnt = 0
                                for rd in os.listdir(DownloadDIR):
                                    if ".jpg" in rd:
                                        cnt += 1
                                        shutil.move(DownloadDIR + "/" + rd, DownloadPath + "/" + New_FOLDER_Name)
                                        sleep(1.5)
                                print("Total IMAGE : ", cnt)
                            except:
                                pass

            elif int(LinkGetStorePageView2_MIN) ==2:
                # print("상가명이 아래에 적혀있슴")
                # 상가명이 아래에 적혀있을시 2부터 시작
                for z in range(int(LinkGetStorePageView2_MIN),int(LinkGetStorePageView2_MAX) + 1):
                    try:
                        time.sleep(1.5)
                        Html = driver.page_source
                        soup = BeautifulSoup(Html, "html.parser")
                        DownloadLinkGetStore1 = soup.find("div", {"class": "optionBox"})
                        DownloadLinkGetStore2 = DownloadLinkGetStore1.find("a").get("href")
                        driver.get(DownloadLinkGetStore2)
                        driver.find_element_by_xpath(
                            '//*[@id="wrap"]/div[2]/div/div/section/div/div[1]/span[2]/button').send_keys('\n')

                    except NoSuchElementException:
                        time.sleep(1.5)
                        driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/span/button[2]').send_keys(
                            '\n')
                        time.sleep(1.5)
                        driver.find_element_by_xpath(
                            '//*[@id="content"]/div/section/div/div/div[3]/div[3]/div[1]/ul').click()
                        Html = driver.page_source
                        soup = BeautifulSoup(Html, "html.parser")
                        DownloadLinkGetStore1 = soup.find("div", {"class": "optionBox"})
                        DownloadLinkGetStore2 = DownloadLinkGetStore1.find("a").get("href")
                        driver.get(DownloadLinkGetStore2)
                        break
                # Total URL Path
                # DirectoryName = " "
                print("FOLDERNAMEHERE", New_FOLDER_Name)

                os.chdir(DownloadPath)  # 현재 작업 디렉토리 변경
                print(os.getcwd())
                os.makedirs(New_FOLDER_Name)
                time.sleep(2)

                try:
                    cnt = 0
                    for rd in os.listdir(DownloadDIR):
                        if ".jpg" in rd:
                            cnt += 1
                            shutil.move(DownloadDIR + "/" + rd, DownloadPath + "/" + New_FOLDER_Name)
                            sleep(1.5)
                            print("Total IMAGE : ", cnt)
                except:
                    pass
        else:
            continue
        print("================= NEXT ===================")
