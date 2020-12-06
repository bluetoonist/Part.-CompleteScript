# userasist 레지스트리
# 암호화 된 레지스트리 키 값 복호화 시키기

lowerLETTERS = [chr(x) for x in range(97, 123)];
upperLETTERS = [chr(x) for x in range(65, 91)];

def rot13(String):
    resultString = "";
    for str_ in String:
        if str_.isupper():
            resultString += encrypt(str_, upperLETTERS);
        elif str_.islower():
            resultString += encrypt(str_, lowerLETTERS);
        else:
            resultString += str_;
    return (resultString)

def encrypt(char, letters):
    retString = '';
    originalIndex = letters.index(char)
    newIndex = originalIndex + 13
    retString += letters[newIndex % len(letters)]
    return retString

def hexToDecimal(param1):
    byteToHexString = param1.hex()
    total = int()
    for x in range(0, len(byteToHexString)):
        if x %2 == 0:
            testA = byteToHexString[x:x+2]+''
            total += int(testA,16)
    return total

from winreg import *

varSubKey = "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" \
            "\\UserAssist\\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\\Count"
Key = CreateKey(HKEY_CURRENT_USER,varSubKey)

for x in range(0,100):
    try:
        a, b, c = EnumValue(Key, x)
        ExecuteFile = rot13(a)
        if ".exe" in ExecuteFile:
            ExecuteNumber = hexToDecimal(b[4:8])
            print(ExecuteFile,ExecuteNumber)
            if "KartRider" in ExecuteFile:
                print(b)

    except Exception as e:
        print(e)


