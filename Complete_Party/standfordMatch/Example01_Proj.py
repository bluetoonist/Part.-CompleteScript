import http.cookiejar
import json
import urllib.parse
import urllib.request

cookiejar = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))

# smile.stanford.edu / Login Function()
def smileEduLogin():
    params = {"username": "", "password": ""}
    params = urllib.parse.urlencode(params)
    params = params.encode("utf8")

    login_url = "https://smile.stanford.edu/smileService/auth/login"

    req = urllib.request.Request(login_url, params)
    opener.open(req)

def readMemberList():
    # return type list
    return_dict = {}

    member_list_url = "https://smile.stanford.edu/smileService/group/456165f0a0b002f5a520355642636f93?_replaceUUIDs%5B0%5D%5B%5D=group.memberIds&" \
                      "_replaceUUIDs%5B0%5D%5B%5D=group.owner&_replace_type%5B%5D=user&_replace_include_fields%5B0%5D%5B%5D=username&" \
                      "_replace_include_fields%5B0%5D%5B%5D=UUID&_replace_include_fields%5B0%5D%5B%5D=firstName&" \
                      "_replace_include_fields%5B0%5D%5B%5D=lastName&" \
                      "_replace_include_fields%5B0%5D%5B%5D=photoUrl&" \
                      "_includeResponses=tru"

    req = urllib.request.Request(member_list_url)
    res = opener.open(req)

    get_member_list_data = res.read().decode()
    # member information
    get_json_list_data = json.loads(get_member_list_data)
    for x in get_json_list_data['group']['memberIds']:
        name_combined = x['lastName'] + x[' firstName']
        member_UUID = x['UUID']

        return_dict[name_combined] = member_UUID

    return return_dict

def readPageQuestionList():
    for x in range(1, 5):
        print("************************************************************************")
        # param1 :  *member list
        # "page" variable  is options
        PageQuestionList = "https://smile.stanford.edu/smileService/resource/topRatedQuestions?orderBy=createdOn&descending=true&" \
                           "resourceType%5B%5D=flippedQuestion&" \
                           "resourceType%5B%5D=openEndedQuestion&page=" + str(x) + "&" \
                                                                                   "_replaceUUIDs%5B0%5D%5B%5D=resources.owner&" \
                                                                                   "_replaceUUIDs%5B0%5D%5B%5D=resources._comments.userId&" \
                                                                                   "_replace_type%5B%5D=user&" \
                                                                                   "_replace_include_fields%5B0%5D%5B%5D=username&" \
                                                                                   "_replace_include_fields%5B0%5D%5B%5D=firstName&" \
                                                                                   "_replace_include_fields%5B0%5D%5B%5D=lastName&" \
                                                                                   "_replace_include_fields%5B0%5D%5B%5D=UUID&" \
                                                                                   "_replace_include_fields%5B0%5D%5B%5D=photoUrl&" \
                                                                                   "_includeResponses=true&_includeAggregates=true&" \
                                                                                   "_includeComments=true&activityId=8da4baf146c58140087b78b0b36a82cc&sessionId=8da4baf146c58140087b78b0b36a90ef"

        # print(PageQuestionList)
        req = urllib.request.Request(PageQuestionList)
        res = opener.open(req)
        get_json_list_data = json.loads(res.read().decode())

        count = len(get_json_list_data["resources"])

        for x, cnt in zip(get_json_list_data["resources"], range(0, count)):
            nameCombined = x['owner']['lastName'] + x['owner']['firstName']
            print("==========================================================")
            print('"', nameCombined, '"', " : ", x['title'])

if __name__ == '__main__':
    smileEduLogin()
    readMemberList()
    readPageQuestionList()
