"""
Speed Test Report 
2019 / 05  / 31 
[+] Process Number : 15 -> 63~ 64 sec 


"""

import Evtx.Evtx as evtx

from xml.etree import ElementTree as ET
from multiprocessing import Process, Manager

path = "C:\Windows\System32\winevt\Logs\Security.evtx"

def Ret4624Count(d,MinNum,MaxNum):
    TotEventNum = 0
    TotalEvent = []

    with evtx.Evtx(path) as log:
        for y in range(MinNum, MaxNum):
            try:
                GetOne = log.get_record(int(y))
                tree = ET.fromstring(GetOne.xml())
                EventId = int(tree[0][1].text)
                if EventId == 4624:
                    TotEventNum += 1
                    TotalEvent += [y]
            except:
                  pass

        d[0] += TotEventNum
        d[1] += TotalEvent

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

if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()
    print(start)
    AllEvent = 0
    with evtx.Evtx(path) as log:
        for _ in log.records():
            AllEvent += 1

    AL = get_list(AllEvent, 11)

    with Manager() as manager:
        d = manager.list([0 for n in range(2)])
        d[1] = []
        MpList = []

        for i in range(0, 10):
            if i == 0:
                MpList.append(Process(target=Ret4624Count, args=(d, 1, AL[0],)))
            MpList.append(Process(target=Ret4624Count, args=(d, AL[i], AL[i + 1],)))

        for _ in MpList:
            _.start()

        for _ in MpList:
            _.join()

        TotalEvent = d[0]
        print(d[0])
        print(len(d[1]))

        stop = timeit.default_timer()
        print(stop-start)
