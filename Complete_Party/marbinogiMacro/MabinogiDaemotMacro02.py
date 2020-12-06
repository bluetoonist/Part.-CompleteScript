import pyautogui
import pywinauto as pwa
import pygetwindow
from time import sleep
import cv2 as cv


Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

# while True:
#     print(pyautogui.position())
# 이미지 찾아서 클릭 테스팅
# Mabinogi_handler.activate()

Mabinogi_handler.resizeTo(1280,1024)

# 이미지 찾아서 클릭 테스팅
Mabinogi_handler.activate()
pyautogui.screenshot("testing.PNG")


for x in range(1,5):
    test_click = pyautogui.locateCenterOnScreen("daemot"+str(x)+".PNG")
    print(x ,"번 쨰 : ",test_click)
