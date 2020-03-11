# -*- coding: utf-8 -*-
from  utils.RequestUtil import Request
from  config.Conf_File import ConfigYaml
from  utils.AssertUtil import AssertUtil
from  utils.MysqlUtil import MySql
#登录
def login():
    Con =ConfigYaml()
    con_url = Con.get_url_yaml()
    url = con_url+"/authorizations/"

    data = {"username":"python","password":"12345678"}

    requset = Request()
    r = requset.post(url,json = data)
    code = r["code"]
    print(code)
    # print(r)
    AssertUtil().assert_code(code,200)
    body = r["body"]
    # print(body,"-------------------")
    # AssertUtil().assert_in_body(body, '"user_id": 1, "username": "python"')

    #初始化数据库对象
    mysql = MySql()

    #调用查询方法
    res_db= mysql.fetchone("select id,username from tb_users where username='python'")
    # print("数据库查询的结果:{}".format(res_db))

    #验证
    user_id = body["user_id"]
    assert  user_id == res_db["id"]
    return r


#查询个人信息
def info():
    url = "http://211.103.136.242:8064/user/"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODMyMTg3MzksInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.7Mh9eeMIhstMNrQQH6qLmwwL0gM_HY5GcsZkvWRsGas"
    header = {
        'Authorization': 'JWT ' + token
    }
    requset = Request()
    r = requset.get(url,headers=header)
    print(r)
    return r



#获取商品列表
def  goods_list():
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
        "page" : "1",
        "page_size" : "10",
        "ordering" : "create_time"
    }
    requset = Request()
    r = requset.get(url,json=data)
    print(r)
    return r


#添加商品到购物车
def  cart():
    url = "http://211.103.136.242:8064/cart/"
    data = {
        "sku_id" : "3",
        "count" : "1",
        "selected" : "true"
    }
    requset = Request()
    r = requset.post(url,json = data)
    print(r)
    return  r



#保存订单
def orders():
    url = "http://211.103.136.242:8064/orders/"
    # data = {"address" : "1", "pay_method" : "1"}
    data = {"address": "1", "pay_method": "1"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODMyMTg3MzksInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.7Mh9eeMIhstMNrQQH6qLmwwL0gM_HY5GcsZkvWRsGas"
    header = {
        'Authorization': 'JWT ' + token
    }
    requset = Request()
    r = requset.post(url, json=data,headers =header)
    print(r)
    return r

if __name__ == "__main__":
    login()
    # info()
    # goods_list()
    # cart()
    # orders()