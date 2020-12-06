import pyautogui
import pywinauto as pwa
import pygetwindow
from time import sleep
import cv2 as cv

# print(pygetwindow.getAllTitles())

Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

for x in range(0,90):
    Mabinogi_handler.activate()
    pyautogui.leftClick(1357,504)
    pyautogui.leftClick(1357,504)
    _handler.activate()
    sleep(0.2)
    print("[" + str(x + 1) + "] 번째 시도중")
Mabinogi_handler.activate()