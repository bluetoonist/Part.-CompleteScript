# 2018.11.25~ 2019.1.25 에서 있었던 목포시 일자리 사업

# 업무자동화 Script 증

# Directory 이름별로 정렬과 정리를 해주는 Script 

import os
import shutil

# Edit Your Path
path = ""

os.chdir(path)

NameList = []
""" Directory Create"""
for rd in os.listdir():
    temp = rd[0:3]
    # print(temp)
    NameList.append(temp)

NameList = sorted(list(set(NameList)))
print(NameList)

try:
    for xd in NameList:
        if len(xd) == 2:
            # print("[-]Not Create Directory :",xd)
            pass
        else:
            print('[+]Success Create Directory :',xd)
            os.makedirs(xd)
except:
    pass
""" Directory Move """
for x in NameList:
    if len(x) == 2:
        pass
    else:
        print("[+] Current Name : " + x)
        for y in os.listdir():
            TempName =y[0:3]
            print(TempName,len(TempName))
            if len(TempName) == 2:
                pass
            else:
                print('->',TempName)
                if x in TempName:
                    shutil.move(path+'\\'+y,path+'\\'+x)
                else:
                    pass

