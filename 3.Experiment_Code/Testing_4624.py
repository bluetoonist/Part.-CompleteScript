# 윈도우 로그파일은 UTC 시간대를 쓰므로 한국시간대로 바꿔서
# 출력을 해야한다. 밑은 그것에 대한 코드.

# 로그인 로그 4624에 대한 이벤트 아이디에 대한 테스트

from threading import *
from Evtx.Views import evtx_chunk_xml_view

import Evtx.Evtx as evtx
from lxml import etree
from bs4 import BeautifulSoup
import threading

path = "C:\Windows\System32\winevt\Logs\Security.evtx"

def transtime(TimeVariable):
    import datetime
    trans_datetime = datetime.datetime.strptime(TimeVariable, "%Y-%m-%d %H:%M:%S")
    time_gap = datetime.timedelta(hours=9)
    kortime = trans_datetime + time_gap
    return kortime

with evtx.Evtx(path) as log:
    AllEvent = 0
    count = 0
    for x in log.records():
        AllEvent += 1

    for y in range(1,AllEvent+1):
        GetOne = log.get_record(int(y))

        soup = BeautifulSoup(GetOne.xml(), "html.parser")
        System_ = soup.find("system")
        Event_ = soup.find("eventdata")
        EventId = int(System_.find("eventid").text)

        if EventId == 4624:

            TimeCreated = System_.find("timecreated").get("systemtime")
            CondenseTime = TimeCreated.split('.')[0]

            OutBound = Event_.find("data",{"name":"IpAddress"}).text
            WorkStationName = Event_.find("data",{"name":"WorkstationName"}).text
            if '-' in OutBound:
                pass
            elif '127.0.0.1' in OutBound:
                pass
            else:
                print(OutBound , CondenseTime, WorkStationName)
