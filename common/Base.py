# -*- coding: utf-8 -*-
import json
import  re
from  utils.RequestUtil import Request
from utils.LogUtil import my_log
import  subprocess
from  config.Conf_File import ConfigYaml
from utils.EmailUtil import SendEmail
#日志
log = my_log()
#定义规则
p_data = '\\${(.*)}\\$'

#格式化字符转换成json
def json_parse(data):
    return json.loads(data) if data else data



#获取前置条件的token并且进行替换
def re_token(handers,token,pattern=p_data,):
    pattern = re.compile(pattern)
    pattern.findall(handers)
    r = re.sub(pattern, token,handers )
    return r


# 进行字段替换
def res_find(data, pattern_data=p_data):
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    log.info("替换过后的值是{}".format(re_res))
    return re_res

#替换
def res_sub(data,replace,pattern_data=p_data):

    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data,replace,data)
    return re_res

#验证是heander是否包含
def params_find(headers,cookies):
    log.info("heanders的值是：{} cookies的值是：{}".format(headers,cookies))
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies


#请求封装
def run_api(url,method,params=None,header=None,cookie=None):
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
        # print(res)
    return res

#执行allure命令
def allure_report(report_path,report_html):
    allure_cmd="allure generate {} -o {} --clean".format(report_path,report_html)
    #allure generate D:\pycode\report\result -o D:\pycode\report\html --clean
    log.info("报告地址：{}".format(allure_cmd))
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("生成日志失败,检查用例环境")
        raise

#邮件配置
def send_mail(report_html_path="",content="",title="测试"):
    emil_info = ConfigYaml().get_emil()
    smtp_addr = emil_info["smtpserver"]
    username = emil_info["username"]
    password = emil_info["password"]
    recv =emil_info["receiver"]
    email = SendEmail(smtp_addr=smtp_addr,
                      username=username,
                      password=password,
                      recv=recv,
                      title=title,
                      content=content,
                      file=report_html_path)
    email.send_mail()