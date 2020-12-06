# -*- coding: utf-8 -*-
# 사용방법은 /n 옵션을 주고 ip가 기록되어 있는 텍스트 파일을 인자로 넣습니다.
# 바토의 API만을 활용합니다.

import requests, json, time, sys, datetime
from pprint import pprint

# VirusTotal의 API를 활용하여 검사 할 파일를 업로드 하여 정보 추출
def virustotal_scan(file):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': ''}
        files = {'file': ('myfile.exe', open(file, 'rb'))}
        response = requests.post(url, files=files, params=params)
        result = response.json()
        return result
    except (IOError, ValueError, TypeError) as e:
        print("virtustota_scan: ", e)
        return False


# VirusTotal의 API를 활용하여 업로드한 파일의 리소스를 이용해 추가 검사 결과 추출
def virustotal_report(resource):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': '', 'resource': resource}
        response = requests.get(url, params=params)
        result = response.json()
        return result
    except (IOError, ValueError, TypeError) as e:
        print("virtustota_report: ", e)
        return False


# VirusTotal의 API를 활용하여 IP 정보 추출
def virustotal_ip(ip):
    parameterIP = ip
    try:
        print("========================= BOX LINE ===========================")
        if "\n" in ip:
            parameterIP = ip.replace("\\n", "")
            parameterIP = str(parameterIP.strip())

        url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
        params = {'apikey': '', 'ip': parameterIP}
        response = requests.get(url, params=params)

        result = json.loads(response.content)
        return result

    except (IOError, ValueError, TypeError) as e:
        print("virtustotal_ip: ", e)


# 악성 IP의 마지막 활동 기간이 10일 내인지 체크
# detected_url은 바토의 결과인지 malwares.com의 결과인지를 구분하기 위한 인자값
def activity_days(today, vato_result_, url):
    activity = None
    active_days = 10

    download = "detected_downloaded_samples"  # Download Sample Check
    communicating = "detected_communicating_samples"  # C&C Check
    date = "date"

    if((communicating in vato_result_) and (download in vato_result_)) and ((len(vato_result_[download]) > 0) and (len(vato_result_[communicating]) > 0)):
        # # 검색된 결과가 "Donwload" 와 "C&C" 둘 다 있을 때
        DnCList = list()

        # 리턴 된 결과값 체크 넘버
        DnCList.append(3)
        activity = vato_result_[download]
        for x in range(len(activity)):
            print(x)
            timeLine = activity[x][date].split(" ")[0]
            cmpTime = datetime.datetime.strptime(timeLine, "%Y-%m-%d").date()
            date_cal = today - cmpTime
            if int(date_cal.days) <= active_days:  # 악성IP 활동 기간이 10일이 넘지 않을 경우 리스트
                DnCList.append(["Download", timeLine])
                break

        activity = vato_result_[communicating]
        for x in range(len(activity)):
            timeLine = activity[x][date].split(" ")[0]
            cmpTime = datetime.datetime.strptime(timeLine, "%Y-%m-%d").date()
            date_cal = today - cmpTime
            if int(date_cal.days) <= active_days:  # 악성IP 활동 기간이 10일이 넘지 않을 경우 리스트 추출
                DnCList.append(["C&C", str(timeLine)])
                break
        return DnCList


    elif (download in vato_result_) and (len(vato_result_[download]) > 0):  # C&C 통신 결과 탐지 항목이 있는지 체크
        activity = vato_result_[download]
        for x in range(len(activity)):
            timeLine = activity[x][date].split(" ")[0]
            cmpTime = datetime.datetime.strptime(timeLine, "%Y-%m-%d").date()
            date_cal = today - cmpTime
            if int(date_cal.days) <= active_days:  # 악성IP 활동 기간이 10일이 넘지 않을 경우 리스트
                return [1, "Download", timeLine]

    elif ((communicating in vato_result_) and len(vato_result_[communicating]) > 0):  # C&C 통신 결과 체크(조회 일 부터 10일 내의 악성IP 추출)

        activity = vato_result_[communicating]
        for x in range(len(activity)):
            timeLine = activity[x][date].split(" ")[0]
            cmpTime = datetime.datetime.strptime(timeLine, "%Y-%m-%d").date()
            date_cal = today - cmpTime
            if int(date_cal.days) <= active_days:  # 악성IP 활동 기간이 10일이 넘지 않을 경우 리스트
                return [2, "C&C", str(timeLine)]

    else:
        return "nothing"


# 악성 IP 로그 출력 및 기록하는 함수
def write_log(write_log, detected_dict, type):
    try:
        # IP 분석 시 저장하는 구문
        if type == "ip_log":
            box_line = "===================================================================\n"
            ip_addr = "[+] IP Address          : "
            vato = "[+] Virustotal RESULT "
            # 악성 IP가 3개 이하 검출될 경우 단순히 화면에 출력하기만 한다.
            if detected_dict.__len__() < 4:
                print("=================== PRINT SCREEN =====================")
                for ip in detected_dict:
                    # print (vato + detected_dict[ip]["v_result"] + " / " + detected_dict[ip]["v_date"] + "\n")
                    pprint(ip)
                    print(box_line)
                return "print screen"

            else:
                print(u"More than 3 analysis requests are saved as log files.")
                detected = dict(detected_dict)

                for ip, data in detected.items():
                    ip = ip.replace("\n", " ")

                    if "Missing IP address" in data:
                        write_log.writelines(ip_addr + str(ip))
                        write_log.writelines("No detected \n")
                        write_log.writelines(box_line)

                    else:
                        write_log.writelines(ip_addr + str(ip))
                        write_log.writelines("\n")
                        write_log.writelines(vato)

                        for x in data:
                            write_log.writelines("\n")
                            write_log.writelines(str(x) + " : " + str(data[x]))
                        write_log.writelines("\n")
                        write_log.writelines(box_line)
                return "written log"
        # 파일 분석 시 저장하는 구문
        else:
            box_line = "===================================================================\n"
            f_name = "- File: %s" % detected_dict["file"]
            f_hash = "- Hash(SHA256): %s" % detected_dict["hash"]
            d_count = "- Detection: %s" % detected_dict["detection_count"]
            write_log.writelines(f_name + "\n")
            write_log.writelines(f_hash + "\n")
            write_log.writelines(d_count + "\n")
            write_log.writelines(box_line + "\n")
            del detected_dict["file"]
            del detected_dict["hash"]
            del detected_dict["detection_count"]
            for vendor in detected_dict:
                write_log.writelines("- Vendor: %s" % vendor + "\n")
                write_log.writelines("- Detected: %s" % detected_dict[vendor][u"detected"] + "\n")
                write_log.writelines("- Name: %s" % detected_dict[vendor][u"result"] + "\n")
                write_log.writelines("- Engine_ver: %s" % detected_dict[vendor][u"update"] + "\n")
                write_log.writelines(box_line + "\n")
            return
    except (IOError, ValueError, TypeError) as e:
        print(e)
        return False


# 바토를 이용한 IP 분석
def ip_analysis(argument):
    ip_dict = {}  # IP당 바토에서 저장되어야할 정보를 저장하기 위해 선언
    misp_ip = []  # MISP_IP는 IP 리스트를 저장

    today = datetime.date.today()  # 오늘 날짜를 체크

    # Argument 옵션이 'i'이면 ip 분석, 옵션이 'n'이면 ip_log
    try:
        # 검사할 IP는 한 개
        if argument[1] == "/i":
            misp_ip.append(str(argument[2]))

        # 검사할 IP 리스트를 읽어들이고 IP 별로 딕셔너리 정리
        elif argument[1] == "/n":
            with open(argument[2], "rt") as rf:

                misp_ip = rf.readlines()
            # IP 리스트가 없으면 프로그램을 빠져나온다.
        if misp_ip.__len__() == 0:
            print("There is no IP address, Please check IP list")
            sys.exit(1)
    except Exception as e:
        print(e)

    # /i 또는 /n 을 통해 입력된 옵션의 IP에 개행문자 또는 공백 문자 제거
    try:
        for count in range(0, len(misp_ip)):
            # IP에 붙어있는 개행문자 제거 후 IP 갯수 만큼 결과 타입을 저장할 딕셔너리 생성
            if "\\n" in misp_ip[count]:
                misp_ip[count] = str(misp_ip[count].replace("\\n", "").strip())

            elif misp_ip[count] is not "":
                ip_dict[misp_ip[count]] = dict()
            else:
                print("A blank line exists. Please check log file")

    except (IOError, ValueError, TypeError) as msg:
        print("- Error message: ", msg)

    try:
        dt = datetime.datetime.now()
        dt = dt.strftime("%Y%m%d%H%M")  # 현재 시각을 구함
        filename = "%s_ip_analysis.log" % dt  # 현재 시각 기준으로 저장할 로그 파일명 정의

        with open(filename, "w") as wf:  # 검사한 IP 중 최근 활동 이력 IP만 기록할 파일

            request_limit = 1  # 바토가 1분에 4번 밖에 검사하지 못해서 요청 리미트 카운트를 둠
            ip_count = 1

            for ip in ip_dict:
                if request_limit > 4:  # 바토가 1분에 4번 밖에 검사가 안 돼서, 5번 째 검사시에는 1분간 대기
                    print(u"- VirusTotal 분 당 최대 분석 수 4개를 초과하여, 1분 후에 수행합니다.")
                    for sec in range(1, 61):
                        print("%d sec\r" % sec, )
                        time.sleep(1)
                    print(u"Initialize analysis limits per minute.")
                    request_limit = 1
                print(u"- Analyzing IP: %s" % ip)
                ip_count += 1

                # request_limit 를 카운트 하는 지점
                request_limit += 1

                try:
                    # virustotal_ip() 안에서 dict로 바꾼 뒤 리턴
                    vato_result = virustotal_ip(str(ip))

                    if vato_result is None:
                        pass

                    if vato_result["response_code"] is 1:
                        detected_url = "VirusTotal"

                        ip_type = activity_days(today, vato_result, detected_url)
                        print(ip_type)
                        if (ip_type == None):
                            ip_dict[ip]["v_result"] = "No detected"
                            ip_dict[ip]["v_date"] = "No detected"
                            continue

                        # 유포지 및 C&C의 검사 결과에 맞게 결과 값 정리
                        if (ip_type[0] is 1) or (ip_type[0] is 2):

                            ip_dict[ip]["v_result"] = ip_type[1]
                            ip_dict[ip]["v_date"] = ip_type[2]

                        elif ip_type[0] is 3:
                            if len(ip_type) == 2:
                                ip_dict[ip]["v_result"] = ip_type[1][0]
                                ip_dict[ip]["v_date"] = ip_type[1][1]
                            elif len(ip_type) == 1:
                                ip_dict[ip]["v_result"] = "No detected"
                                ip_dict[ip]["v_date"] = "No detected"

                            else:
                                ip_dict[ip]["v_result_Download"] = ip_type[1][0]
                                ip_dict[ip]["v_result_C&C"] = ip_type[2][0]
                                ip_dict[ip]["v_date_Download"] = ip_type[1][1]
                                ip_dict[ip]["v_date_C&C"] = ip_type[2][1]
                    else:
                        ip_dict[ip]["v_result"] = "No detected"
                        ip_dict[ip]["v_date"] = "No detected"

                except (IOError, ValueError, TypeError) as e:
                    print(e)
                    continue




            # 검사 결과를 파일로 잘 저장했을 경우 성공 메시지를, 실패했을 경우 파일 I/O 체크 권고 메시지 발생
            log_result = write_log(wf, ip_dict, "ip_log")
            print(log_result)

            if log_result == "print screen":
                print("Result completed.")
            elif log_result == "written log":
                print("Result completed. More than 3 analysis requests are saved in '%s' file" % filename)
            else:
                print("Detected works failed, Attempt to verify file I/O")
            print("============================================================")

    except (IOError, ValueError, TypeError) as msg:
        print("- Error message : ", msg)
        pass


# 바토를 활용한 file 분석
def file_analysis(argument):
    if "\\" in argument[2] or "/" in argument[2]:
        pass
    else:
        argument[2] = argument[0][:argument[0].rfind("/") + 1] + argument[2]
    result = virustotal_scan(argument[2])
    if result is not False and result[u"response_code"] is 1:
        result = virustotal_report(result[u"resource"])

        # 업로드 한 파일의 분석 완료 시간이 있기 때문에 5초마다 분석 완료 상태를 체크, 총 5번 반복으로 무한루프를 회피
        analysis_count = 0
        while result[u"response_code"] == -2:
            print("Now Analyzing... please wait a moment\r", )
            time.sleep(5)
            result = virustotal_report(result[u"resource"])
            if analysis_count < 5:
                analysis_count += 1
            else:
                print("[%d] File analysis failed, Try to check error code by Web site" % result[u"response_code"])
                sys.exit(1)
        if result[u"positives"] > 0:
            ext_result = result[u"scans"]
            file_name = argument[2][argument[2].rfind("\\") + 1:]
            ext_result["file"] = file_name
            ext_result["hash"] = result[u"sha256"]
            ext_result["detection_count"] = str(result[u"positives"]) + "/" + str(result[u"total"])
            dt = datetime.datetime.now()
            dt = dt.strftime("%Y%m%d%H%M")
            log_file = "%s_file_analysis.log" % dt
            with open(log_file, "wt") as wf:  # 검사한 IP 중 최근 활동 이력 IP만 기록할 파일
                write_log(wf, ext_result, "file_log")
            print("Result completed. analysis requests are saved in '%s' file" % log_file)
        else:
            print("Not detected on all AV_Engine")
    else:
        print("Failure: Check if any parameters or files exist.")


# 메인 함수, 이 함수를 통해 각 함수들이 호출 됨.
def main(argv):
    if argv[1] in ("/i", "/n"):
        ip_analysis(argv)
    else:
        file_analysis(argv)


if __name__ == "__main__":
    # 정상적인 옵션을 사용할 경우 메인 함수로 이동

    if sys.argv.__len__() is 3 and sys.argv[1].lower() in ("/i", "/n", "/f"):
        sys.argv[1] = sys.argv[1].lower()
        main(sys.argv)

    # 정상적인 옵션을 제대로 입력 못했을 경우 사용 방법 출력
    else:
        path = sys.argv[0]
        print(u"\n[Use example]\n")
        print(u"- %s /i 8.8.8.8" % path[path.rfind("\\") + 1:])
        print(u"- %s /n ip_list.log" % path[path.rfind("\\") + 1:])
        print(u"- %s /f test.exe\n" % path[path.rfind("\\") + 1:])
        print(u"[Option description]\n")
        print(u"  [/i]: Use Virustotal to verify single IP Address\n")
        print(u"  [/n]: Use Virustotal and Malwares.com to verify multiple IP address (need a log file)\n")
        print(u"  [/f]: Use Virustotal to verify malware file\n")