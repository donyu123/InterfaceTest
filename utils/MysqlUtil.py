# -*- coding: utf-8 -*-

#导入sql包
import  pymysql
from  utils.LogUtil import my_log

class  MySql:

    #初始化连接数据库
    def __init__(self):
        self.log = my_log("数据库日志")
        self.conn = pymysql.connect(
            host="211.103.136.242",
            user="test",
            password="test123456",
            database="meiduo",
            charset="utf8",
            port=7090
            )

    #创建查询方法 查询单个
    def  fetchone(self,sql):
        #把查的结果以字典形式进行储存
        self. cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        #执行sql
        try:
            self.cursor.execute(sql)
            # 查询一条或多条
            res = self.cursor.fetchone()
        except:
            self.log.error("执行单个查询方法失败")
        return res

    #创建查询方法 查询多个
    def fetchall(self,sql):
        try:
            #把查的结果以字典形式进行储存
            self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            #执行sql
            self.cursor.execute(sql)
            #查询多条
            res = self.cursor.fetchall()
        except:
            self.log.error("执行多个查询方法失败")
        return res

    #关闭连接
    def __del__(self):
        #关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        #关闭数据库连接
        if self.conn  is not None:
            self.conn.close()

# a = MySql()
# print(a.fetchone("select id,username from tb_users where username='python'"))
# #连接数据库
# conn  = pymysql.connect(
#     host="211.103.136.242",
#     user="test",
#     password="test123456",
#     database="meiduo",
#     charset="utf8",
#     port=7090
#     )
# #获取执行的光波
# cursor = conn.cursor()
# #编写sql语句
# sql = "select username,password from tb_users"
# #执行sql
# cursor.execute(sql)#查询一条或多条
# res = cursor.fetchone()
# print(res)
# #关闭对象
# cursor.close()
# #关闭数据库
# conn.close()