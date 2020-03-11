# -*- coding: utf-8 -*-
from config.Conf_File import ConfigYaml
from common.ExcelData import Data
from common.ExcelConfig import ExcelConfig
import  pytest
from  common.Base import json_parse
from  common.Base import params_find,res_sub,run_api,allure_report,send_mail
import  allure
from  config import Conf_File
import os

#获取测试用例 文档 并且打开 调用判断方法 判断哪条用例可执行
run_list = Data("D:/pycode/data/testdata.xlsx","美多商城接口测试")

#获取根据是否运行字段的测试用例
data_init=run_list.get_run_data()

#实例化对应excel字段的类
data_key = ExcelConfig()

#获取sheet名称
sheet_name = ConfigYaml().ger_sheet_name()
class TestExcel:

    #执行前置用例
    def  run_pre(self,data_pre):
        #拼接url
        url = ConfigYaml().get_url_yaml()+data_pre[ExcelConfig().url]
        method = data_pre[data_key.method]
        params = data_pre[data_key.params]
        headers = data_pre[data_key.headers]
        cookies = data_pre[data_key.cookies]

        #判断headers cookise是否存在，json转义，
        header = json_parse(headers)
        cookie = json_parse(cookies)

        res = run_api(url,method,params,header,cookie)
        print("前置用例执行",res)
        return res


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
            # 执行前置用例
            pre_res= self.run_pre(data_pre)
            headers,cookies = self.get_correlation(headers,cookies,pre_res)


        # 获取yml文件的接口url地址 获取excel接口路径 拼成url地址
        url = ConfigYaml().get_url_yaml() + url
        header = json_parse(headers)
        cookie = json_parse(cookies)
        r = run_api(url, method, params, header, cookie)
        print("测试用例执行：%s" % r)

        #allure
        #获取一级标签 也就是表格的sheet名称
        allure.dynamic.feature(sheet_name)
        #获取模块story二级标签
        allure.dynamic.story(case_model)
        #获取用例id和接口名称
        allure.dynamic.title(case_id+case_name)
        #设置备注 有请求的url 请求类型 期望结果 实际结果描述
        desc = "<font color = 'red'>请求url：</font>{}</Br>"\
               "<font color = 'red'>请求类型：</font>{}</Br>"\
               "<font color = 'red'>期望结果：</font>{}</Br>"\
               "<font color = 'red'>实际结果：</font>{}</Br>".format(url,method,expect_result,r)

        allure.dynamic.description(desc)
        return r


    #关联先获取当前headers 和cookis  查询是否有内容   有就进行替换
    def get_correlation(self, headers, cookies, pre_res):
        # 验证handers中是否有内容
        headers_para, cookies_para = params_find(headers, cookies)
        # 判断  headers_para是否为空
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            print(".............",headers_data)
            # 结果替换
            headers = res_sub(headers, headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = res_sub(headers, cookies_data)
            # print("cookies",cookies)
        return headers, cookies

if __name__ == "__main__":
    # 日志报告json文件
    report_path = Conf_File.get_report_path() + os.sep + "result"
    # 日志报告
    report_path_html = Conf_File.get_report_path() + os.sep + "html"
    #执行请求 并且生成报告json文件
    pytest.main(["-s","test_excel_case.py","--alluredir",report_path])

    # #调用生成报告方法 转换成html文件
    # allure_report(report_path,report_path_html)
    # #发送邮件
    # send_mail(title="接口测试报告",content=report_path_html)
