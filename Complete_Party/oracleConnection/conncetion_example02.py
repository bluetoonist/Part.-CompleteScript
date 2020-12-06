# -*- coding:utf-8 -*-
# 동적 쿼리를 생성하기 위한 예제
import cx_Oracle
from random import *

connection = cx_Oracle.connect()
cur = connection.cursor()

farmid_list = [1, 2, 3, 5, 7, 187, 188, 201, 225, 245, 246, 247, 248, 249, 187, 188, 250]

tankid = ['전복', '넙치']
state = ["G", "Y", "R"]

for _ in range(50):
    tankid_select = randint(0, 1)
    farmid_select = randint(0, 16)
    fishid_select = randint(1, 10)
    state_select = randint(0, 2)

    watertank_do = round(uniform(1, 9.5), 1)
    watertank_wtrec = round(uniform(1, 32), 1)
    watertank_phrec = round(uniform(1, 12), 1)
    watertank_nh4rec = round(uniform(1, 40), 1)
    watertank_no2rec = round(uniform(1, 20), 1)

    sql_query = "INSERT INTO rec VALUES (recseq.NEXTVAL," + "'" + str(tankid[tankid_select]) + "'" + "," + str(
        farmid_list[
            farmid_select]) + "," + str(fishid_select) + "," + "'" + str(
        state[state_select]) + "'" + " ,null ,SYSDATE ," + str(watertank_do) + "," + str(watertank_wtrec) + ",1," + str(
        watertank_phrec) + "," + str(watertank_nh4rec) + "," + str(
        watertank_no2rec) + ",SYSDATE ,'sysadmin' ,SYSDATE ,'sysadmin')"
    print(watertank_do, watertank_wtrec, watertank_phrec, watertank_nh4rec, watertank_no2rec)
    print(sql_query)

    cur.execute(sql_query)

connection.commit()
cur.close()
