import sys
import socket
import Evtx.Evtx as evtx

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup,SoupStrainer
from multiprocessing import Process, Manager

path = "C:\Windows\System32\winevt\Logs\Security.evtx"

"""
#  Process Work Divide : get_list(num,p)
## 파라미터 설명
    1. num  : 멀티프로세싱을 위한 전체 Event 로그의 갯수를 매개 변수로 받습니다. 
    2. p    : 몇개의 작업으로 분할 할 것인지 매개 변수로 받습니다.

## 기능 설명
    전체 Event 로그의 갯수를 인자로 받고 p 의 갯수만큼 작업을 분할한 뒤
    분할한 수 만큼 누적 리스트로 만든 다음 리턴합니다.
"""
def get_list(num,p):
    result = 0
    list1 = []
    allocate = int(num/p)

    for x in range(p):
        list1.append(allocate)
    list1[p-1] += (num%p)+1

    for x, y in zip(list1, range(0, len(list1))):
        result += x
        list1[y] = result
    return list1


"""
#  MultiProcessing Event Counter : Ret4624Count(d,MinNum,MaxNum)
## 파라미터 설명
    1. d       : 멀티프로세스의 Manager() 객체를 통해 넘겨받는 공유될 리스트
    2. MinNum  : 작업을 시작할 로그 Record의 최소값
    3. MaxNum  : 작업을 끝마칠 로그 Record의 최대값

## 기능 설명
    이 함수는 Manager()를 통해 넘겨 받은 공유 리스트의
    첫 번째 인덱스에, Event ID가 4624인 것의 갯수를 리턴합니다.
    두 번째 인덱스에, Event ID가 4624인 것들의 숫자를 리스트로 만들어 리턴합니다.
"""

def Ret4624Count(d,MinNum,MaxNum):
    select_Event = SoupStrainer("system")
    with evtx.Evtx(path) as log:
        TotEventNum = 0
        TotalEvent = []
        for y in range(MinNum, MaxNum):
            try:
                GetOne = log.get_record(int(y))
                soup = BeautifulSoup(GetOne.xml(), "lxml", parse_only=select_Event)
                EventId = int(soup.find("eventid").text)

                if EventId == 4624:
                    TotEventNum += 1
                    TotalEvent += [y]
            except Exception as e:
                pass
        d[0] += TotEventNum
        d[1] += TotalEvent

"""
# Change to Korean Time : transtime(TimeVariable)
##  파라미터 설명
    TimeVariable : 날짜 형식을 매개변수로 받습니다 (날짜 형식 : "2019-05-28 12:34:56")

## 기능 설명
    로그 파일에 기록된 날짜 형식은 한국 시간과 9시간 정도의 시차가 발생하는데, 그 시간을
    한국 시간대로 바꿔주는 기능을 함
"""
def transtime(TimeVariable):
    # print(TimeVariable)
    Ret = TimeVariable.split('.')[0]

    import datetime
    trans_datetime = datetime.datetime.strptime(Ret, "%Y-%m-%d %H:%M:%S")
    time_gap = datetime.timedelta(hours=9)
    kortime = trans_datetime + time_gap
    return kortime


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250,220,250,220)
        self.setWindowTitle("Log 분석")

        # Login Log Table Form
        # 로그인 로그 분석을 진행한뒤 결과를 보여줄 테이블 UI
        self.tableWidget = QTableWidget()
        self.tableWidget.setWindowTitle("Login LOG Analysis")
        self.move(500, 500)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnToContents(12)

        # Rdp Log Table Form
        # RDP 로그 분석을 진행한 뒤 결과를 보여줄 테이블 UI
        self.tableWidgetRdp = QTableWidget()
        self.tableWidgetRdp.setWindowTitle("RDP Log Analysis")
        self.move(500, 500)
        self.tableWidgetRdp.resizeColumnsToContents()
        self.tableWidgetRdp.resizeRowsToContents()
        self.tableWidgetRdp.resizeColumnToContents(12)

        # Progress Bar
        # 진행 상태를 나타내 줄 % 바
        self.progress = QProgressBar(self)
        self.progress.setGeometry(20,200,230,15)
        self.progress.setMaximum(100)

        # 간편 인증입니다
        # 입력한 MD5 메시지와 일치하면 다음 기능을 이용하고 불일치 하면 프로그램이 종료됩니다.
        self.LoginMD5()


        """
        Host Name UI - Start Line
        HOST 이름을 가져오고 결과를 옆의 QLineEdit에 보여준다.
        
        """
        HostName = QLabel(self)

        font1 = HostName.font()
        font1.setPointSize(11)

        HostName.setFont(font1)
        HostName.setText("PC 이름 :")
        HostName.setAlignment(Qt.AlignLeft)
        HostName.setGeometry(30,20,130,130)

        HostName_Line = QLineEdit(self)
        HostName_Line.setFont(font1)
        HostName_Line.setText(self.GetHostName())
        HostName_Line.move(200,200)
        HostName_Line.setGeometry(100,18,130,20) # x,y, width,heigh


        """
        IP Addr UI  - Start Line 
        공인 IP 주소를 가져오고 그 IP 주소를 옆의 QLineEdit에 보여준다.
        """
        GetIpAddr = QLabel(self)
        GetIpAddr.setFont(font1)
        GetIpAddr.setText("IP  주소 :")
        GetIpAddr.setAlignment(Qt.AlignLeft)
        GetIpAddr.setGeometry(30, 60, 130, 130)

        GetIpAddr_Line = QLineEdit(self)
        GetIpAddr_Line.setFont(font1)
        GetIpAddr_Line.setText(self.GetIpAddr())
        GetIpAddr_Line.move(200,200)
        GetIpAddr_Line.setGeometry(98,57,130,20)


        """
        PlatForm UI - Start Line
        PlatForm 정보를 가져오고 그 IP 주소를 옆의 QLineEdit에 보여준다.
        """
        PlatFormLabel = QLabel(self)
        PlatFormLabel.setFont(font1)
        PlatFormLabel.setText("System  :")
        PlatFormLabel.setAlignment(Qt.AlignLeft)
        PlatFormLabel.setGeometry(30, 100, 130, 130)

        PlatFormLine = QLineEdit(self)
        PlatFormLine.setFont(font1)
        PlatFormLine.setText(self.FindPlatForm())
        PlatFormLine.move(200,200)
        PlatFormLine.setGeometry(98,98,130,20)

        # RDP Log Analysis
        Rdpbtn = QPushButton("RDP로그 분석",self)
        Rdpbtn.setGeometry(20,130,100,60)
        Rdpbtn.clicked.connect(self.RdpAnalysis)
        Rdpbtn.show()

        # Login Log Analysis
        LoginLog = QPushButton("Login로그 분석", self)
        LoginLog.setGeometry(140, 130, 100, 60)
        LoginLog.clicked.connect(self.LoginAnalysis)
        LoginLog.show()
        self.show()

    # Get Host Name Function
    def GetHostName(self):
        PcHostName = str(socket.gethostname())
        return PcHostName

    # Get Ip Address Function
    def GetIpAddr(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return str(s.getsockname()[0])

    # Get Plat Form Name Function
    def FindPlatForm(self):
        import platform
        PlatForm = platform.platform()
        return str(PlatForm)

    # 완성된 기능
    # MD5로 암호화된 특정 메시지를 입력해야 기능을 이용할 수 있습니다.
    def LoginMD5(self):
        text, okPressed = QInputDialog.getText(self, "Authentication", "Input The MD5:", QLineEdit.Normal, "")
        if okPressed:
            if "979A0E192A27373E913C29A7B2477DAE" in text:
                pass
            else:
                exit()

        if okPressed == False:
            exit()


    def closeEvent(self, event):
        Answer = QMessageBox.question(self, "종료", "종료확인", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if Answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # RDP LOG Analysis
    def RdpAnalysis(self):
        RdpAllEvent = 0
        RowCount = 0
        Rdppath = "C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx"
        with evtx.Evtx(Rdppath) as log:
            for _ in log.records():
                RdpAllEvent += 1
                soup = BeautifulSoup(_.xml(), "lxml")

                System_ = soup.find("system")
                EventId = int(System_.find("eventid").text)

                if EventId == 1149:
                    RowCount += 1

        self.tableWidgetRdp.setRowCount(RowCount)
        self.tableWidgetRdp.setColumnCount(4)

        with evtx.Evtx(Rdppath) as log:
            EventCounter = 0
            for x in range(1, RdpAllEvent + 1):
                try:
                    CurrentProg = "%d" % int((x / RdpAllEvent) * 100)
                    print(CurrentProg)
                    self.progress.setValue(int(CurrentProg))

                    getone = log.get_record(x)
                    soup = BeautifulSoup(getone.xml(), "lxml")

                    System_ = soup.find("system")
                    EventId = int(System_.find("eventid").text)

                    UserData = soup.find("userdata")

                    if EventId == 1149:
                        TimeCreated = System_.find("timecreated").get("systemtime")
                        CondenseTime = str(transtime(TimeCreated.split('.')[0]))
                        UserName = UserData.find("param1").text
                        UserPcName = UserData.find("param2").text
                        AccessIP = UserData.find("param3").text

                        RdpTempList = [CondenseTime, UserName, UserPcName, AccessIP]


                        for floop, sloop in zip(range(0, len(RdpTempList)), RdpTempList):
                            self.tableWidgetRdp.setColumnWidth(floop, 200)
                            self.tableWidgetRdp.setItem(EventCounter, floop, QTableWidgetItem(sloop))
                        EventCounter += 1

                except UnicodeDecodeError:
                    pass
        self.tableWidgetRdp.show()

        print("[+] RDP Analysis Done !")

    # Login Analysis
    def LoginAnalysis(self):
        AllEvent = 0
        with evtx.Evtx(path) as log:
            for _ in log.records():
                AllEvent += 1

        AL = get_list(AllEvent, 10)

        with Manager() as manager:
            d = manager.list([0 for n in range(2)])
            d[1] = []
            MpList = []
            for i in range(0, 9):
                if i == 0:
                    MpList.append(Process(target=Ret4624Count, args=(d, 1, AL[0],)))
                MpList.append(Process(target=Ret4624Count, args=(d, AL[i], AL[i + 1],)))

            for _ in MpList:
                _.start()

            for _ in MpList:
                _.join()

            TotalEvent = d[0]

            self.tableWidget.setRowCount(TotalEvent)
            self.tableWidget.setColumnCount(6)

            EventIdCounting = 0
            d[1] = sorted(d[1])

            with evtx.Evtx(path) as log:
                for p1 ,p2 in zip( d[1] , range(0,len(d[1])) ):
                    CurrentLog =  "%d"%int( (p2/len(d[1])) * 100 )
                    self.progress.setValue(int(CurrentLog))
                    print(CurrentLog)
                    try:
                        GetOne = log.get_record(int(p1))

                        #system xml
                        soup = BeautifulSoup(GetOne.xml(), "lxml")

                        System_ = soup.find("system")
                        Event_ = soup.find("eventdata")
                        EventId = int(System_.find("eventid").text)

                        # 로그인 로그에 대한 이벤트 ID
                        if EventId == 4624:
                            TimeCreated = soup.find("timecreated").get("systemtime")
                            CondenseTime = str(transtime(TimeCreated.split('.')[0]))

                            UserName = Event_.find("data", {"name": "TargetUserName"}).text  # 유저이름
                            IpAddr = Event_.find("data", {"name": "IpAddress"}).text  # IP 주소
                            WorkStationName = System_.find("computer").text  # 컴퓨터이름
                            LogonType = Event_.find("data", {"name": "LogonType"}).text  # 로그온 유형
                            SecurityID = Event_.find("data", {"name": "SubjectUserSid"}).text

                            tmp = [CondenseTime, UserName, IpAddr, WorkStationName, SecurityID, LogonType]

                            for sloop, Lloop in zip(range(0, 7), tmp):
                                self.tableWidget.setColumnWidth(sloop,200)
                                self.tableWidget.setItem(EventIdCounting, sloop, QTableWidgetItem(Lloop))
                            del tmp
                            EventIdCounting += 1
                    except UnicodeDecodeError:
                        pass

            self.tableWidget.show()
            print("[+] Login Analysis Done !")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())