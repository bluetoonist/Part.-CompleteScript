import urllib.request
import urllib.parse

'''
 국가지도서비스(vworld)를 이용한 위도와 경도 찾기 Script

'''


# BaseUrl = "http://api.vworld.kr/req/address?"
BaseUrl2 = "http://apis.vworld.kr/new2coord.do?"

# Edit Search Address 
address = ''

# Your API KEY 
ApiKey = ''

Values = {
'q':address,
'apiKey':ApiKey,
'domain':'http://api.vworld.kr/',
'output':'json',
'epsg':'EPSG:4326'
}

param = urllib.parse.urlencode(Values)

Adding = BaseUrl2+param

req = urllib.request.Request(Adding)
res = urllib.request.urlopen(req)

SaveData = res.read().decode()
print(SaveData)
import ast

Dataing =ast.literal_eval(SaveData)
latitude = Dataing['EPSG_4326_Y']
longitude = Dataing['EPSG_4326_X']

print('위도:',latitude,'경도:',longitude)
print("==================================")
print("주소:",address)


