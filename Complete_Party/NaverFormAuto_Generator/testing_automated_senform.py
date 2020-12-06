import random

from time import sleep
# selenium module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\\Users\\user\\Desktop\\Source\\PythonSource\\crawlingtool\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print("==================  [+] Start ==================== ")

# 몇 번 시도
form_url = "https://form.office.naver.com/form/responseView.cmd?formkey=MzY2NGM2ZTAtMmE4Zi00MmRlLWI4ZTAtN2NjNTA4Mjc1ZGI1"

driver.find_element_by_xpath('//*[@id="formItem_31"]/div/div[2]/div/div[2]/div').click()