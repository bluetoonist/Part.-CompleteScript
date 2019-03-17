import requests
from bs4 import BeautifulSoup

for x in range(4608,5000):
    EventId = x
    """ Microsoft Window EventID"""
    UrlPath = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-" + str(EventId)

    r = requests.get(UrlPath)
    html = r.content.decode()

    soup = BeautifulSoup(html, "html.parser")
    EventExplain = soup.find("main", {"id": "main"})
    EventTitle = EventExplain.find("h1").text

    if "404" in EventTitle:
        pass
    else:
        print(EventTitle)


# for x in range(4608,5000):
#     EventId = x
#
#     """ Microsoft Window EventID"""
#     UrlPath = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-" + str(EventId)
#
#     r = requests.get(UrlPath)
#     html = r.content.decode()
#
#     soup = BeautifulSoup(html, "html.parser")
#
#     EventExplain = soup.find("main", {"id": "main"})
#     for rd in EventExplain.find_all("p"):
#         if not (rd.find("strong")):
#             print(rd.text)
#     print("====================================================")