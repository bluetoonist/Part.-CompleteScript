import pyautogui
import pywinauto as pwa
import pygetwindow
from time import sleep
import cv2 as cv

# print(pygetwindow.getAllTitles())

Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

Mabinogi_handler.resizeTo(1280,1024)
character_Postion_x,character_Postion_y = Mabinogi_handler.center

Mabinogi_handler.activate()

# while True:
#     print(pyautogui.position())


for x in range(1,20):
    pyautogui.screenshot("rock"+str(x)+".png", region=(1349,504, 40, 40))

# 이미지 찾아서 클릭 테스팅
for x in range(1,20):
    test_click = pyautogui.locateCenterOnScreen("rock"+str(x)+".png")
    # point_x ,point_y = test_click
    print(x ,"번 쨰 : ",test_click)
    pyautogui.leftClick(test_click)
    pyautogui.leftClick(test_click)