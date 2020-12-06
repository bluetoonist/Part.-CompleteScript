import pyautogui
import pygetwindow
from time import sleep
import random

#  특정 좌표를 기준으로 클릭하는 매크로
Mabinogi_handler =  pygetwindow.getWindowsWithTitle("마비노기")[0]
Exit_handler =  pygetwindow.getWindowsWithTitle("Program Manager")[0]

Mabinogi_handler.resizeTo(1280,800)
character_Postion_x,character_Postion_y = Mabinogi_handler.center

pyautogui.moveTo(character_Postion_x, character_Postion_y)

Mabinogi_handler.activate()

pyautogui.press('a')

for x in range(1,10):
    r = random.randint(1,50)
    pyautogui.moveTo(character_Postion_x , character_Postion_y % r)
    pyautogui.leftClick(character_Postion_x , character_Postion_y)



# for x in range(1,100):
#     pyautogui.press('a',interval=10)
# for x in range(0,90):
#     Mabinogi_handler.activate()
#     pyautogui.leftClick(character_Postion_x+120,character_Postion_y)
#     pyautogui.leftClick(character_Postion_x+120,character_Postion_y)
#     _handler.activate()
#     sleep(0.2)
#     percentage = int((x / 89) * 100)
#     if percentage % 25 == 0:
#         print("[" + str(int(percentage)) + "]%")
#     else:
#         pass
# Mabinogi_handler.activate()