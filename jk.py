#coding=utf-8
import requests
from flask import Flask,session,jsonify
import datetime
# 1. 组装请求
# url = "http://httpbin.org/get"  # 这里只有url，字符串格式
# 2. 发送请求，获取响应
# res = requests.get(url) # res即返回的响应对象
# 3. 解析响应
# print(res.text)  # 输出响应的文本

# a = raw_input("请输入聊天内容：")
# b = raw_input("请回复聊天内容：")
# url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"
# res = requests.get(url=url)
# print(res.text)

# username = 'admin'
# password = '123456'

# app = Flask(__name__)
# app.secret_key = 'pithy'

# @app.route('/login',methods = ['GET','POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username']!= username:
#             error = 'Invalid username'
#         elif request.form['password'] != password:
#                 error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             return jsonify({'code':200,'msg':'success'})
#         return jsonify({'code':401,'msg':error}),401
# @app.route('/info',methods = ['get'])
# def info():
#     if not session.get('logged_in'):
#         return jsonify({'code':401,'msg':'please login '})
#     return jsonify({'code':200,'msg':'success','data':'info'})
# if __name__ == '_main_':
#     app.run(debug = True )


class User():
    def __init__ (self,full_name,birthday):
        self.name = full_name
        self.birthday = birthday

        name_splits = full_name.split(' ')
        self.first_name = name_splits[0]
        self.last_name = name_splits[-1]
    def age(self):
        today = datetime.date(2020,1,1)
        years = int(self.birthday[0:4])
        month = int(self.birthday[4:6])
        days = int(self.birthday[6:8])

        birthday_date = datetime.date(years,month,days)
        how_old_in_days = (today - birthday_date).days
        how_old_in_years = how_old_in_days/365

        return int(how_old_in_years)


user1 = User('willan li','19880907')
print user1.age()
# print user1.first_name
# print user1.last_name
# print user1.birthday

class MyClass:
    i=12345
    def f(self):
        return 'hello world'

x=MyClass()
print("MyClass  i :",x.i)
print("MyClass f :",x.f())