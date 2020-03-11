# -*- coding: utf-8 -*-
from config.Conf_File import ConfigYaml
from common.ExcelData import Data
from common.ExcelConfig import ExcelConfig
from  utils.RequestUtil import Request
from utils.LogUtil import my_log
import  pytest
from  common.Base import json_parse
from  common.Base import re_token,params_find

#获取测试用例 文档 并且打开 调用判断方法 判断哪条用例可执行
run_list = Data("../data/testdata.xlsx","美多商城接口测试")

#获取根据是否运行字段的测试用例
data_init=run_list.get_run_data()
#日志
log = my_log()
#实例化对应excel字段的类
data_key = ExcelConfig()
class TestExcel:

    #请求封装
    def run_api(self,url,method,params=None,header=None,cookie=None):
        # 接口请求
        reqest = Request()
        #验证parrams 是否有内容
        params = json_parse(params)

        if str(method).lower() == "get":
            res = reqest.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = reqest.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("I like you")
        return res

    #执行前置用例
    def  run_pre(self,data_pre):
        #拼接url
        url = ConfigYaml().get_url_yaml()+data_pre[ExcelConfig().url]
        method = data_pre[data_key.method]
        params = data_pre[data_key.params]
        headers = data_pre[data_key.headers]
        cookies = data_pre[data_key.cookies]

        #判断headers cookise是否存在，json转义，无需
        header = json_parse(headers)
        cookie = json_parse(cookies)

        res = self.run_api(url,method,params,header,cookie)
        # print("前置用例执行",res)
        # self.token=res["body"]["token"]
        return res
        # print(token)
    #增加pytest查找到根据是否运行 获取的用例
    @pytest.mark.parametrize("case",data_init)
    def  test_run(self,case):

        #获取excel内的各项key

        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        url = case[data_key.url]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]


        if pre_exec:
            # 获取是前置条件测试用例
            data_pre = run_list.get_run_pre(pre_exec)
            # print("前置条件的测试用例为{}".format(data_pre))
            pre_res= self.run_pre(data_pre)
            headers, cookies = self.get_correlation(headers, cookies, pre_res)
            print("---",pre_res)


        # 获取yml文件的接口url地址 获取excel接口路径 拼成url地址
        url = ConfigYaml().get_url_yaml() + url
        # 判断headers cookise是否存在，json转义，
        header = json_parse(headers)

        # print("hander的值是",header)
        cookie = json_parse(cookies)
        r = self.run_api(url, method, params, header, cookie)
        print("测试用例执行：%s" % r)
        return r

    def get_correlation(self,headers,cookies,pre_res):
        headers_para, cookies_para = params_find(headers, cookies)
        # 有关联，执行前置用例，获取结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            print(headers_data)
            # 结果替换
            headers = re_token(headers, headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = re_token(headers, cookies_data)
            print("cookies", cookies)
        return headers, cookies


if __name__ == "__main__":
    pytest.main(["-s","test_excel_case1.py"])


