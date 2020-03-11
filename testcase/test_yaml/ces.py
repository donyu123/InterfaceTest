# -*- coding: utf-8 -*-
#
# res=[{'用例ID': 'Info_2', '模块': '个人信息', '接口名称': '获取个人信息正确', '请求URL': '/user/', '前置条件': 'login_4', '请求类型': 'get', '请求参数类型': '', '请求参数': '', '预期结果': "id': 1, 'username': 'python', 'mobile': '17701397029', 'email': '952673638@qq.com'", '实际结果': '', '备注': '', '是否运行': 'y', 'headers': '{"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODM0ODM3NTgsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.CKG5j9FerYqMOtVKUhuEWwmOxjDWuT9mxPy6wa4kNbs"}', 'cookies': '', 'status_code': 200.0, '数据库验证': "select id,username,mobile,email from tb_users where username='python'"}]
#
# run_list =[{'用例ID': 'login_1', '模块': '登录', '接口名称': '登录参数为空', '请求URL': '/authorizations/', '前置条件': '', '请求类型': 'POST', '请求参数类型': 'json', '请求参数': '', '预期结果': '无效数据。期待为字典类型', '实际结果': '', '备注': '', '是否运行': 'n', 'headers': '', 'cookies': '', 'status_code': 400.0, '数据库验证': ''},
# {'用例ID': 'login_2', '模块': '登录', '接口名称': '登录名为空', '请求URL': '/authorizations/', '前置条件': '', '请求类型': 'POST', '请求参数类型': 'json', '请求参数': '{"username":"","password":"12345678"}', '预期结果': "username': ['该字段不能为空。']", '实际结果': '', '备注': '', '是否运行': 'n', 'headers': '', 'cookies': '', 'status_code': 400.0, '数据库验证': ''},
# {'用例ID': 'login_3', '模块': '登录', '接口名称': '登录名或密码为空', '请求URL': '/authorizations/', '前置条件': '', '请求类型': 'POST', '请求参数类型': 'json', '请求参数': '{"username":"","password":""}', '预期结果': "password': ['该字段不能为空。']", '实际结果': '', '备注': '', '是否运行': 'n', 'headers': '', 'cookies': '', 'status_code': 400.0, '数据库验证': ''},
# {'用例ID': 'login_4', '模块': '登录', '接口名称': '登录成功', '请求URL': '/authorizations/', '前置条件': '', '请求类型': 'POST', '请求参数类型': 'json', '请求参数': '{"username":"python","password":"12345678"}', '预期结果': "user_id': 1, 'username': 'python'", '实际结果': '', '备注': '', '是否运行': 'n', 'headers': '', 'cookies': '', 'status_code': 200.0, '数据库验证': ''}]
#
#
# pre_exec  = res[0]["前置条件"]
#
#
# run =run_list
# for line in  run:
#     print("-----",line)
#     if pre_exec in dict(line).values():
#         print(line)
#

str1 = '{"Authorization": "JWT ${token}$"}'
#定义规则
import  re
pattern=re.compile('\${(.*)}\$')
res =pattern.findall(str1)
token = "123"
r=re.sub(pattern,token,str1)
print(r)
#执行用例 判断是否有前置条件 如果有 先去执行前置条件  拿到前置条件的token 进行替换把前置条件的token放该接口内