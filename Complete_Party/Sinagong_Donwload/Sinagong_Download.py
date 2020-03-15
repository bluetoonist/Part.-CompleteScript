# 2019.04.12 완성
# 시나공 홈페이지의 오픈된 자료 다운로드 스크립트
import os,wget
import zipfile

# 다운로드 받을 폴더 경로
FilePath = "D:\\Py_Source\\Info_src\\Download\\"

# 다운로드 범위 지정 (게시물의 idx)
for x in range(1000,10000):
    try:
        url = 'https://sinagong.gilbut.co.kr/download?type=PDS_FILE&idx='+str(x)
        print(wget.download(url,FilePath+str(x)+".zip"))

    except Exception as e:
        print("[-]404 Not Found",str(x))

# 다운로드 받은 파일에 "기사" 나 "정" 이라는 단어가 있으면 압축을 품
for ld in os.listdir(FilePath):
    if ".zip" in ld:
        try:
            with zipfile.ZipFile(FilePath + '\\' + ld) as f:
                zipinfo = f.infolist()

                for member in zipinfo:
                    member.filename = member.filename.encode("cp437").decode("euc-kr")

                    if "기사" in str(member.filename) or "정" in str(member.filename):
                        print(member.filename)
                        f.extract(member,path=FilePath)
                    else:
                        pass
        except Exception as e:
            pass
    else:
        pass
