# Mokpo BIZ  IMAGE UPLOAD 2019 1/11 완성본
# 2018.11.25~ 2019.1.25 에서 있었던 목포시 일자리 사업
# 업무자동화 Script 증
# 이미지 업로드시 에러가 났을 때 주요기능 분리

import time
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\\Users\\MokpoBIZ\\PycharmProjects\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

# registration
# Setup Image Directory setup

BaseDIR = ""
for ld in os.listdir(BaseDIR):
    driver.find_element_by_class_name("add_photo").send_keys(Keys.ENTER)

    try:
        driver.find_element_by_xpath('//*[@id="photo_0"]').send_keys(BaseDIR + ld)
        time.sleep(0.2)
        driver.find_element_by_xpath('//*[@id="upload"]').send_keys('\n')
        time.sleep(1)
        # driver.switch_to_alert().accept()
        Alert(driver).accept()
        time.sleep(1.5)
        # driver.switch_to_alert().accept()
        Alert(driver).accept()

    except UnexpectedAlertPresentException:
        Alert(driver).accept()
    except:
        Alert(driver).accept()
