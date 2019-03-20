# Note
# 현재까지 작업한 통합코드 이 파일을 통해 완성시킬 것

# 2019 03 29 -> 필요한 모니터링 유형 과 권장 사항을 스크래핑해서 가져오도록 추가


import sys
import time
import requests

from collections import Counter

from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import Evtx.Evtx as evtx

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.counter = 1

    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.setText("C:\Windows\System32\winevt\Logs\Security.evtx")
        self.textbox.move(120,10)
        self.textbox.resize(370,30)

        self.textbox2 = QTextBrowser(self)
        self.textbox2.move(10,45)
        self.textbox2.resize(480,450)

        self.button = QPushButton("LogFilePath",self)
        self.button.move(10,10)

        self.button.clicked.connect(self.on_click)
        self.show()

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Font Dialog")
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()

        whiteList = [4624,4625,4648,4675]

        with evtx.Evtx(textboxValue) as log:
            record = log.get_record(self.counter)
            soup = BeautifulSoup(record.xml(),"html.parser")
            system_ = soup.find("system")

            # EventId Filter
            EventId = int(system_.find("eventid").text)

            print(EventId)
            for wlist in whiteList:
                if wlist == EventId:
                    print("Current=>",wlist)
                    UrlPath = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-" + str(
                        EventId)

                    r = requests.get(UrlPath)
                    html = r.content.decode()

                    soup = BeautifulSoup(html, "html.parser")
                    EventExplain = soup.find("main", {"id": "main"})
                    EventTitle = EventExplain.find("h1").text

                    table = soup.find_all("table")[1]

                    f1 = table.find_all("td")
                    print(len(f1))
                    str1 = "필요한 모니터링 권장사항\n "
                    str2 = "권장사항\n "
                    for cnt in range(len(f1)):
                        if cnt % 2 != 0:
                            # 권장 사항
                            tmp = table.find_all("td")[cnt]
                            str2 += tmp.text + '\n\n'
                        else:
                            tmp = table.find_all("td")[cnt]
                            str1 += tmp.text + '\n\n'

                    self.textbox2.setText(EventTitle+'\n\n'+str1+'\n\n'+str2)

                else:
                    pass

            self.counter = self.counter+1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
