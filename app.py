# -*- coding:utf-8 -*-
from flask import Flask, request
import json
import pymysql
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
app = Flask(__name__)

def makequestion:
    connect = pymysql.connect(host='localhost', user='root', password='패스워드', db='DB명',\
                          charset='utf8mb4')
    cur = connect.cursor()

    query = 
    cur.excute(query)
    connect.commit()
    #데이터 베이스 두번째에 있는 설명부분을 가지고 온다
    question = #데이터 베이스에서 가지고 오기
    answerlist = #보기 1 , 보기 2, 보기 3
    answer = #데이터 베이스 앞에꺼

    return 

def db_create():
    engine = create_engine("postgres://"uxweficayqkvnb:191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f@ec2-54-225-234-165.compute-1.amazonaws.com:5432/ddtk33j69v200c", echo = False)

@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody

if __name__ == "__main__":
    app.run(port=5000)