import pyautogui
import pywinauto as pwa
import pygetwindow
from time import sleep
import cv2 as cv

Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

Mabinogi_handler.resizeTo(1280,1024)
character_Postion_x,character_Postion_y = Mabinogi_handler.center

for x in range(0,90):
    Mabinogi_handler.activate()
    pyautogui.leftClick(character_Postion_x+120,character_Postion_y)
    pyautogui.leftClick(character_Postion_x+120,character_Postion_y)
    _handler.activate()
    sleep(0.2)
    percentage = int((x / 89) * 100)
    if percentage % 25 == 0:
        print("[" + str(int(percentage)) + "]%")
    else:
        pass
Mabinogi_handler.activate()