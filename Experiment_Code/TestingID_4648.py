# 윈도우 로그파일은 UTC 시간대를 쓰므로 한국시간대로 바꿔서
# 출력을 해야한다. 밑은 그것에 대한 코드.

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

        if EventId == 4648:

            TimeCreated = System_.find("timecreated").get("systemtime")
            CondenseTime = TimeCreated.split('.')[0]
            TargetServerInfo = Event_.find("data",{"name":"TargetInfo"}).text
            TargetServerName = Event_.find("data",{"name":"TargetServerName"}).text
            if "localhost" in TargetServerInfo:
                pass
            else:
                print(TargetServerInfo,TargetServerName)


