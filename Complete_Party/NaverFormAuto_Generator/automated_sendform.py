import random

from time import sleep
# selenium module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\\Users\\user\\Desktop\\Source\\PythonSource\\crawlingtool\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print("==================  [+] Start ==================== ")

# 몇 번 시도
for x in range(0,15):

    print("["+str(x)+"] 번쨰 시도")
    form_url = "https://form.office.naver.com/form/responseView.cmd?formkey=MzY2NGM2ZTAtMmE4Zi00MmRlLWI4ZTAtN2NjNTA4Mjc1ZGI1"

    driver.get(form_url)
    # 1. 응답자 본인의 소속을 선택해주세요.
    # 소속 선택 : 대학생 고정
    driver.find_element_by_xpath('//*[@id="formItem_31"]/div/div[2]/div/div[2]/div/div[1]').click()
    sleep(1)
    # 2. 본인이 본교 재학생이시면 소속대학을 선택해 주세요. (8문항)
    #  공과대 1
    #  자연과학대 2 ~ 8
    # 단과대 선택 xpath : //*[@id="formItem_14"]/div/div[2]/div/div["여기 번호 선택"]/div/div[1]
    choice_number = str(random.randint(1, 8))
    driver.find_element_by_xpath('// *[ @ id = "formItem_14"] / div / div[2] / div / div[1] / div / div[1]').click()
    sleep(0.5)

    # 3. 2019 MNU 페스티벌 행사에 어느정도 만족하셨나요?* (5문항)
    # 1 매우 만족, 2 만족 , 3 보통 ,4 불만족 ,5 매우 불만족
    choice_number = str(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="formItem_33"]/div/div[2]/div/div['+choice_number+']/div/div[1]').click()

    # 4. 2019 MNU 페스티벌에서 가장 기억에 남는 프로그램은 무엇인지 선택해 주세요.* (5문항)
    choice_number = str(random.randint(1, 5))
    driver.find_element_by_xpath('//*[@id="formItem_2"]/div/div[2]/div/div[5]/div/div[1]').click()

    # 5. 2019 MNU 페스티벌에서 가장 만족하시는 프로그램은 무엇인지 선택해 주세요.* (5문항 중 성택 (총 6문항) )
    choice_number = str(random.randint(1, 6))
    driver.find_element_by_xpath('//*[@id="formItem_17"]/div/div[2]/div/div[4]/div/div[1]').click()

    # 7. 2019 MNU 페스티벌에서 가장 준비가 미흡한 프로그램은 무엇인지 선택해 주세요.* (6문항 중 성택 (총 7문항) )
    choice_number = str(random.randint(1, 6))
    driver.find_element_by_xpath('//*[@id="formItem_21"]/div/div[2]/div/div[6]/div/div[1]').click()

    # 8. 2019 MNU 페스티벌 준비사항, 참여 및 참관의 편의성 정도를 선택해 주세요. (5문항)
    choice_number = str(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="formItem_22"]/div/div[2]/div/div['+choice_number+']/div/div[1]').click()

    # 9. 내년에도 이와 같은 행사가 개최된다면 참석 여부에 대하여 선택해주세요* (3문항)
    choice_number = str(random.randint(1, 3))
    driver.find_element_by_xpath('//*[@id="formItem_20"]/div/div[2]/div/div['+choice_number+']/div/div[1]').click()

    driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]').click()
    sleep(2)

print("==================  [-] End ==================== ")