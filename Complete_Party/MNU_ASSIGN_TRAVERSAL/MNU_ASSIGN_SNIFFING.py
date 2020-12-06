
import wget
import os

with open("NameList.txt" ,"r",encoding="utf8") as f:
    for x in f.readlines():
        gradeNumber,Name,MajorInfo = x.split(" ")[0].split("\t")
        guess_string = gradeNumber+"_"+Name+".hwp"
        url_string = guess_string.encode("euc-kr")

        guess_string = str(url_string).replace('\\x','%')[2:-1]
        url ="http://cyber.mokpo.ac.kr/servlet/service.common.updown.DownloadServlet?webDir=/upload/classroom/report/9994/0/REPORT_1575701678073&fileNm="+guess_string
        wget.download(url)

    for x in f.readlines():
        gradeNumber,Name,MajorInfo = x.split(" ")[0].split("\t")
        guess_string = gradeNumber+"_"+Name+"6"+".hwp"
        url_string = guess_string.encode("euc-kr")

        guess_string = str(url_string).replace('\\x','%')[2:-1]
        url ="http://cyber.mokpo.ac.kr/servlet/service.common.updown.DownloadServlet?webDir=/upload/classroom/report/9994/0/REPORT_1575701678073&fileNm="+guess_string
        wget.download(url)

for x in os.listdir():
    if "service.common" in x:
        os.remove(x)