# How To Use urllib Login

# Target Site : http://mail.mokpo.ac.kr

# Current Successfully Worked 2019/02/27

import http.cookiejar
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup
from getpass import getpass

cj = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

Id = str(input("Your ID : "))
Pw = str(getpass("Your Password : "))

# Urlencode parameter
values = {
    "LoginID":Id,
    "x":"0",
    "y":"0",
    "password":Pw,
    "p_lang":""
}
BaseURL = "http://mail.mokpo.ac.kr/"
url = "http://mail.mokpo.ac.kr/login_pool.jsp"
url2 = "http://mail.mokpo.ac.kr/setIP.jsp"

MailBoxURL = "http://mail.mokpo.ac.kr/leftmenu.jsp?color=red&gw_sms=null&gw_mail=true"

params = urllib.parse.urlencode(values)
params = params.encode("utf8")

req1 = urllib.request.Request(url,params)
res1 = opener.open(req1)

MailParsing = ""

try:
    GetMailBox = urllib.request.Request(MailBoxURL,params)
    respone = opener.open(GetMailBox)
    content = respone.read()
    MailParsing+=content.decode("utf8")

except Exception as e:
    print(e)

# Filtering List Data
UrlFilter1 = []
UrlFilter2 = []
UrlFilter3 = []

MailLIst = []

UrlFilter1 += MailParsing.split(';')

for rd in UrlFilter1:
    if "\r\n" in  rd:
        UrlFilter2.append(rd.replace("\r\n",''))
del UrlFilter1

for rd in UrlFilter2:
    if "\t" in rd:
        UrlFilter3.append(rd.replace('\t',''))
    else:
        UrlFilter3.append(rd)
del UrlFilter2

for rd in UrlFilter3:
    SaveMailIndex = rd.find("list.jsp?")
    SaveMailIndex2 = rd.find("')")
    if SaveMailIndex != -1:
        ClearUrl = rd[SaveMailIndex::].replace("')",'')
        MailLIst.append(ClearUrl)

GetMailBox = urllib.request.Request(BaseURL+MailLIst[0], params)
res2 = opener.open(GetMailBox)

soup = BeautifulSoup(res2,"html.parser")
Table_Find = soup.find("td",{"width":"100%"})
Table_Find2 = Table_Find.find("table",{"class":"dataTable"})

DataString = ""

for rd in Table_Find2.findAll("td"):
    DataString += rd.text

DataString = DataString.strip()

ScrapingSplitList= []
ScrapingSplitList2 = []
ScrapingSplitList3 = []
print("====  Scraping ! ====")

for rd in DataString:
   if ' ' == rd:
        ScrapingSplitList.append(' ')
   if ' ' != rd:
        ScrapingSplitList.append(rd)

tmpstr = str()
for rd in ScrapingSplitList:
    if rd != '\xa0':
        tmp = []
        tmpstr += rd
        tmp.append(tmpstr)

    elif rd == '\xa0':
        ScrapingSplitList2.append(tmp)
        tmpstr = str()

for rd,count in zip(ScrapingSplitList2,range(len(ScrapingSplitList2))):
    tmp = []
    try:
        if ScrapingSplitList2[count] == ScrapingSplitList2[count+1]:
            ScrapingSplitList3.append(ScrapingSplitList2[count])
        if count+1 == max(range(len(ScrapingSplitList2))):
            ScrapingSplitList3.append(ScrapingSplitList2[count])
            ScrapingSplitList3.append(ScrapingSplitList2[count+1])

    except:
        pass

from pprint import pprint
pprint(ScrapingSplitList3)
