"""
Comment:
    목포 해양수산청 홈페이지의  직원 목록을 가져와서 '이름'으로 검색을 할 수 있게 만든 코드

#2018.01.05
     동명이인 이면 후에 넣은 데이터가 뒤집어 써짐
#2018.01.08
    32bit : 1~10 까지 11~19 까지 짜름
    64bit 일 떄는 for i range(1~19) 로 수정
#2018.01.09
    뒤 쪽 페이지에 있는 이름 검색이 안되는 것 수정

OS:
    Windows 7 Professional K(32bit) ,
    RAM 4GB ,
    CPU : intel Core(TM) i5-6500 3.20GHz
IDE:
    Pycharm Community
    Python 3.6.2
    Chrome Driver
"""
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
url = 'http://mokpo.mof.go.kr/im/userList.do'
driver.get(url)

Name,Name2 = [],[]  # 이름을 담기 위한 리스트형
sub_list,sub_list2 = [],[]  # 이름에 대한 검색 정보 매칭
First_DB,Second_DB = {},{}
print("[+] Appending ")
# 1~10
for i in range(1, 9):
    driver.execute_script("cfnPageLink(" + str(i) + ")")  # java script 함수를 실행 시키기 위한 .excute_script

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    tables = soup.find("tbody", {"class": "tb_center"})
    table = tables.find_all("tr")  # 페이지의 tr 태그를 찾음

    for tag in tables.find_all("tr"):
        Add_Name = tag.find_all('td')[0].get_text()  # tr의 첫번쨰 td 태그(이름) 을 가져오는 소스
        Name.append(Add_Name)

    for tag2 in table:
        tag2 = tag2.get_text().replace('\n', ' ')  # tr 태그의 '\n'를 공백(한 칸 띄운)으로 대체
        tmp = [tag2]
        sub_list.append(tmp)

for name, info in zip(Name, sub_list):
    First_DB[name] = info

# 11~19
for i in range(9, 19):
    driver.execute_script("cfnPageLink(" + str(i) + ")")  #JavaScript 함수를 실행 시키기 위한 .excute_script

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    tables = soup.find("tbody", {"class": "tb_center"})
    table = tables.find_all("tr")  # 페이지의 tr 태그를 찾음

    for tag in tables.find_all("tr"):
        Add_Name = tag.find_all('td')[0].get_text()  # tr의 첫번쨰 td 태그(이름) 을 가져오는 코드
        Name2.append(Add_Name)

    for tag2 in table:
        tag2 = tag2.get_text().replace('\n', ' ')  # tr 태그의 '\n'를 공백(한 칸 띄운)으로 대체
        tmp = [tag2]
        sub_list2.append(tmp)

for nam2, info2 in zip(Name2, sub_list2):
    Second_DB[nam2] = info2

driver.close()

while True:  # 이름 검색 로직
    try:
        find = str(input("INput Name:"))
        if find == 'z':
            break
        if find in First_DB:
            print(First_DB[find])
        if find in Second_DB:
            print(Second_DB[find])
    except:
        pass
    else:
        continue


