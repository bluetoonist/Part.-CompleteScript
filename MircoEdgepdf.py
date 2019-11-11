#-*- coding:utf8 -*-
# 2019.05.09 Complete

import psutil

MicroEdge = []
MicroEdgePid = []
print("[+] MicrosoftEdge 사용자가 보고 있는 문서 ")
for p in psutil.process_iter():
    if "MicrosoftPdfReader.exe" in p.name():
        MicroEdgePid.append(p.pid)

for pid in MicroEdgePid:
    p1 = psutil.Process(pid)
    for x in p1.as_dict()['memory_maps']:
        if ".pdf" in x.path:
            print(x.path)
