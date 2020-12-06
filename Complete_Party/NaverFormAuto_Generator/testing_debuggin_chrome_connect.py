# Debugging chrome 연결 테스팅 코드

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
path = "C:\\Users\\user\\Desktop\\Source\\PythonSource\\crawlingtool\\chromedriver_win32\\chromedriver.exe"
chrome_driver = path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

# 연결이 잘 된다면 아래 주소로 이동함
driver.get("http://www.naver.com")