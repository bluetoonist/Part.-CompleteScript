#  발생한 Eventid의 내용을 Microsoft 에서 가져옴

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

        whiteList = [4663,4656,4658,4660,4657,5039,4670,4608,4624]
        with evtx.Evtx(textboxValue) as log:
            record = log.get_record(self.counter)
            soup = BeautifulSoup(record.xml(),"html.parser")
            system_ = soup.find("system")

            # EventId Filter
            EventId = int(system_.find("eventid").text)

            print(EventId)
            for wlist in whiteList:
                if wlist == EventId:
                    UrlPath = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-" + str(
                        EventId)

                    r = requests.get(UrlPath)
                    html = r.content.decode()

                    soup = BeautifulSoup(html, "html.parser")
                    EventExplain = soup.find("main", {"id": "main"})
                    EventTitle = EventExplain.find("h1").text

                    if "404" in EventTitle:
                        pass
                    else:
                        self.textbox2.setText(str(wlist)+"\n"+EventTitle)


                else:
                    pass

            self.counter = self.counter+1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
