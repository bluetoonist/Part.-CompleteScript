import pyautogui
import pywinauto as pwa
import pygetwindow
from time import sleep
import cv2 as cv

# print(pygetwindow.getAllTitles())

Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

# while True:
#     print(pyautogui.position())
# pyautogui.screenshot("rock2.png",region=(13,520,30,30))

for x in range(1,100):
    pyautogui.screenshot("rock"+str(x)+".png", region=(1310+x, 496+x, 30, 30))


# 이미지 찾아서 클릭 테스팅
# Mabinogi_handler.activate()
# for x in range(1,100):
#     test_click = pyautogui.locateCenterOnScreen("rock"+str(x)+".png")
#     print(x ,"번 쨰 : ",test_click)

