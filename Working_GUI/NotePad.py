import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import Evtx.Evtx as evtx

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(120,10)
        self.textbox.resize(370,30)

        self.button = QPushButton("Input Log File",self)
        self.button.move(10,10)

        self.button.clicked.connect(self.on_click)
        self.show()

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Font Dialog")
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()

        with evtx.Evtx(textboxValue) as log:
            print(log.get_file_header())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())