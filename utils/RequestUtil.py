# -*- coding: utf-8 -*-
import  requests

class   Request:

    #把接口参数进行封装
    def request_api(self,url,data=None,json=None,headers=None,cookies=None,method="get"):

        #判断请求是get还是post
        if method == "get":
            r = requests.get(url,data=data,json=json,headers=headers,cookies=cookies)

        elif method == "post":
            r = requests.post(url,data=data,json=json,headers=headers,cookies=cookies)

        #获取请求的状态
        code = r.status_code
        try:
        #获取请求的数据
            body = r.json()
        except Exception as e :
        #如果报错就返回该文本
            body = r.text

        #把请求状态 和请求数据 合成字典
        res = dict()
        res["code"] = code
        res["body"] = body

        #返回字典
        return  res

    #对外提供get post调用方法
    def get(self,url,**kwargs):
        return  self.request_api(url,method="get",**kwargs)

    def post(self,url,**kwargs):
        return  self.request_api(url,method="post",**kwargs)