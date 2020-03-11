# -*- coding: utf-8 -*-
from utils.LogUtil import my_log
import  json
class AssertUtil:

    def __init__(self):
        self.log = my_log("AssertUtil日志")

    #code 验证 返回的状态码是否正确
    def assert_code(self,code,expected_code):
        try:
            assert  int(code) == int(expected_code)
            return True
        except:
            self.log.error("{} {} 状态码错误".format(code,expected_code))
            raise

    #验证body是否相等
    def assery_body(self,body,expeected_body):
        try:
            assert  body == expeected_body
            return  True
        except:
            self.log.error("{} {} 内容不相等".format(body,expeected_body))
            raise
    #验证是否body包含你期望的数据
    def assert_in_body(self,body,expeected_body):
        try:
            body = json.dumps(body)
            assert  expeected_body in body
            return  True
        except:
            self.log.error("不包含{} {}".format(body,expeected_body))
            raise