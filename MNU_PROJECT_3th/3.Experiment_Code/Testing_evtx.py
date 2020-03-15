# Evtx Package Usage Example

import Evtx.Evtx as evtx
import Evtx.Views as e_views

FilePath = "C:\Windows\System32\winevt\Logs\Security.evtx"

import json
from pprint import pprint
from bs4 import BeautifulSoup

"""  All Parsing """
with evtx.Evtx(FilePath) as log:
    record = log.get_record(1)
    print(record.xml())

    soup = BeautifulSoup(record.xml(), "html.parser")
    system_ = soup.find("system")
    EventId = system_.find("eventid").text

    # TimeCreated = system_.find("timecreated").get("systemtime")
    print(EventId)

    """Get All record Information"""
    # for record in log.records():
    #     soup = BeautifulSoup(record.xml() ,"html.parser")
    #     system_ = soup.find("system")
    #     EventId = system_.find("eventid").text
    #
    #     TimeCreated = system_.find("timecreated").get("systemtime")
    #     print(EventId,"==",TimeCreated)


""" One Object Parsing """
# with evtx.Evtx(FilePath) as evtx:
#     record = evtx.get_record(40)
#     if record is None:
#         raise RuntimeError("Cannot find the record specified.")
#     output = str(record.xml())
#     soup = BeautifulSoup(output,'html.parser')
#     system_ = soup.find("system")
#     EventId = system_.find("eventid").text
#     print(EventId)
#
#     f = open("./output.html","w")
#     f.write(output)

""" If you Have logfile to .html"""
# f = open("./output.html","r")
# soup = BeautifulSoup(f,"html.parser")
#
# system_ = soup.find("system")
# print(system_)
# EventId = system_.find("eventid").text
# TimeCreated = system_.find("timecreated").get("systemtime")
# print(EventId,TimeCreated)

# print("===============================")
# event_= soup.find("eventdata")
# print(event_)
# SubjectUserSid = event_.find("data",{"name":"SubjectUserSid"}).text
# SubjectUserName = event_.find("data",{"name":"SubjectUserName"}).text

# print(SubjectUserSid,"?!",SubjectUserName)
# f.close()
