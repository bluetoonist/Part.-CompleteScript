# Function -> EventID Counting

import Evtx.Evtx as evtx
import Evtx.Views as e_views
import requests

from collections import Counter
from bs4 import BeautifulSoup

FilePath = "C:\Windows\System32\winevt\Logs\Security.evtx"
MicrosoftURL = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-"

GarvageList = []

"""  All Parsing """
with evtx.Evtx(FilePath) as log:
    """Get All record Information"""
    for record in log.records():
        soup = BeautifulSoup(record.xml() ,"html.parser")
        system_ = soup.find("system")

        EventId = system_.find("eventid").text
        TimeCreated = system_.find("timecreated").get("systemtime")

        r = requests.get(MicrosoftURL+str(EventId))
        html = r.content.decode()

        soup = BeautifulSoup(html, "html.parser")
        EventExplain = soup.find("main", {"id": "main"})
        EventTitle = EventExplain.find("h1").text

        if "404" in EventTitle:
            pass
        else:
            Eid,Contents = EventTitle.split(":")
            GarvageList.append(Eid.split(' ')[0])
            print(Eid.split(' ')[0])

            print(Counter(GarvageList))

print(Counter(GarvageList))