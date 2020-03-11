# -*- coding: utf-8 -*-
import  os
from  utils.YamlUtil import YamlReader

#获取当前文件目录
cruuent = os.path.abspath(__file__)

#获取当前项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(cruuent))
# print(BASE_DIR)

#定义config目录
_config_path = BASE_DIR +os.sep +"config"
# print(_config_path)

#拼接conf.yml文件路径
config_file = _config_path +os.sep+"conf.yml"
# print(config_file)

#获取数据库yml文件路径
db_file = _config_path+ os.sep+"db_conf.yml"
# print(db_file)

#report报告路径
_report_path = log_path = BASE_DIR + os.sep+"report"
print(_report_path)
def  get_report_path():
    return  _report_path

#提供调用yml文件路径方法
def  get_config_yml():
    return  config_file

#定义logs文件夹路径
log_path = BASE_DIR + os.sep+"logs"
print(log_path)

#提供对外拼接路径的log日志方法方法
def get_log_path():
    return  log_path

#提供对外使用的dbconf.yml文件路径
def get_db_file():
    return db_file

#创建类 读取yml文件
class  ConfigYaml:
    #初始化方法 读取yaml文件
    def  __init__(self):
        self.con = YamlReader(get_config_yml()).data()
        self.db = YamlReader(get_db_file()).data()

    #提供对外读取yaml url数据的方法
    def get_url_yaml(self):
        return self.con["BASE"]["test"]["url"]

    #提供对外读取yaml log leve等级的方法
    def get_log_level(self):
        return  self.con["BASE"]["log_level"]

    #提供对外读取yaml 日志后缀方法
    def get_log_extension(self):
        return  self.con["BASE"]["log_extension"]

    #设置数据库
    def get_db(self,db_alias):
        return self.db[db_alias]

    #获取测试用例的sheet名称
    def ger_sheet_name(self):
        return self.con["BASE"]["test"]["sheet_name"]

    #读取邮箱数据
    def get_emil(self):
        return  self.con["BASE"]["emil"]

if __name__ =="__main__":
    con = ConfigYaml()
    # c= con.ger_sheet_name()
    c = con.get_emil()
    # c = con.get_log_level()
    # c = con.get_log_extension()
    # c= con.get_db("db_1")
    print(c)
