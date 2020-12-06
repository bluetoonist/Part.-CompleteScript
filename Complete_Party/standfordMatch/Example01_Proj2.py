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
    request_test_url = "https://smile.stanford.edu/smileService/resource/topRatedQuestions?orderBy=createdOn&" \
                  "descending=true&" \
                  "resourceType%5B%5D=flippedQuestion&" \
                  "resourceType%5B%5D=openEndedQuestion&page=3&" \
                  "_replaceUUIDs%5B0%5D%5B%5D=resources.owner&" \
                  "_replaceUUIDs%5B0%5D%5B%5D=resources._comments.userId&" \
                  "_replace_type%5B%5D=user&_replace_include_fields%5B0%5D%5B%5D=username&" \
                  "_replace_include_fields%5B0%5D%5B%5D=firstName&" \
                  "_replace_include_fields%5B0%5D%5B%5D=lastName&" \
                  "_replace_include_fields%5B0%5D%5B%5D=UUID&" \
                  "_replace_include_fields%5B0%5D%5B%5D=photoUrl&" \
                  "_includeResponses=true&_includeAggregates=true&" \
                  "_includeComments=true&activityId=8da4baf146c58140087b78b0b36a82cc&" \
                  "sessionId=8da4baf146c58140087b78b0b36a90ef"

    req = urllib.request.Request(request_test_url)
    res = opener.open(req)

    get_read_data = res.read().decode()
    get_json_transfer_data = json.loads(get_read_data)

    print(get_json_transfer_data)

    from pprint import pprint

    for x in get_json_transfer_data['resources']:
        if x['UUID'] in "8da4baf146c58140087b78b0b3870444":
            pprint(x)


if __name__ == '__main__':
    smileEduLogin()
    readMemberList()
