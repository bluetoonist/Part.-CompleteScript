# Python 3.6.7 에서 동작
# Oracle instantClient 19.x 버전이 시스템 환경변수로 잡혀져 있어야 됨,

import os
# connection 되어 얻어온 정보가 한글이 깨져있을 떄
os.putenv('NLS_LANG','.UTF8')

import cx_Oracle

connection = cx_Oracle.connect("DB_ID","DB_PASSWORD","DB_CONNCETION(IP:PORT:SID")

cur = connection.cursor()

query = "select * from farm"

cur.execute(query)

for x in cur:
    print(x)

connection.close()
