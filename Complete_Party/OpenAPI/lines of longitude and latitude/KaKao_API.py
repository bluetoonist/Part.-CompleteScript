# Daum Map KaKao API를 이용한
# 위도와 경도 입력시 KTM 좌표계 변환

import urllib.request
import urllib.parse
API_KEY = "KakaoAK {Your API KEY}"

RestURL = "https://dapi.kakao.com/v2/local/geo/transcoord?"

#경도 longitude
#위도  latitude

x=''
y=''

Values = {

    # '''KTM 좌표계 변환'''
    'x':x,
    'y':y,
    'input_coord':'WGS84',
    'output_coord':'KTM',
}

param = urllib.parse.urlencode(Values)
Adding = RestURL+param

req = urllib.request.Request(Adding)
req.add_header('Authorization',API_KEY)
res = urllib.request.urlopen(req)

result = res.read().decode()

import ast
b1 = ast.literal_eval(result)

KTM_X = b1['documents'][0]['x']
KTM_Y = b1['documents'][0]['y']

print("KTM X 값 : ",KTM_X)
print("KTM Y 값 : ",KTM_Y)
