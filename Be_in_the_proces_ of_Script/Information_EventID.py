"""
각 EventID 마다 양식이 다르기 때문에
각 EventID 마다 Function을 생성해
Main()에서 Callable 가능하도록 추가 중

!Note
2019 03 21 : 로그온 감사 EventID 4624,4625,4648 Scrap

"""
from bs4 import BeautifulSoup
import requests

def GetHtml(EventId):
    MicroWindoSecu = "https://docs.microsoft.com/ko-kr/windows/security/threat-protection/auditing/event-"
    UrlPath = MicroWindoSecu + str(EventId)
    r = requests.get(UrlPath)
    html = r.content.decode()
    soup = BeautifulSoup(html, "html.parser")
    return soup

# LogON Auditing
def Scrap_id_4624(EventId=4624):
    soup = GetHtml(EventId)
    table = soup.find_all("table")[1]
    f1 = table.find_all("td")
    str1,str2 = "",""
    for cnt in range(len(f1)):
        if cnt % 2 != 0: # 권장 사항
            tmp = table.find_all("td")[cnt]
            str2 += tmp.text + '\n'
        else: # 보안 모니터링 사항
            tmp = table.find_all("td")[cnt]
            str1 += tmp.text + '\n'
    print("권장 사항")
    print(str2)
    print("보안 모니터링 사항")
    print(str1)

# LogON Auditing
def Scrap_id_4625(EventId=4625):
    soup = GetHtml(EventId)
    Information4625 = ""
    SecuAlarm = soup.find_all("ul")[22]
    Information4625 += SecuAlarm.text
    SecuAlarm2 = soup.find_all("ul")[23]
    for x in range(7):
        tmp = SecuAlarm2.find_all("li")[x]
        Information4625 += tmp.text
    print(Information4625)

def Scrap_id_4648(EventId=4648):
    soup = GetHtml(EventId)
    table = soup.find_all("table")[0]
    tabletd = table.find_all("td")
    str1, str2 = "필요한모니터링유형\n ", "권장사항\n "
    for x in range(len(tabletd)):
        if x % 2 != 0:  # 권장사항
            tmp = table.find_all("td")[x]
            str2 += tmp.text + '\n'
        else:  # 필요한 모니터링 유형
            tmp = table.find_all("td")[x]
            str1 += tmp.text + '\n'
    print(str1, str2)
