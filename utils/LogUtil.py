# -*- coding: utf-8 -*-
import  logging
from config.Conf_File import *
import datetime
import  os
#定义日志级别的映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR

}
#创建类
class  Logger:

    #初始化方法 名称 存放日志文件路径  日志级别
    def __init__(self,log_name,log_file,log_level):
        self.log_name = log_name
        self.log_file = log_file
        self.log_level = log_level

        #设置控制台名称
        self.logger  = logging.getLogger(self.log_name)
        #设置日志级别
        self.logger.setLevel(log_l[self.log_level])

        # 判断hander是否存在
        if not self.logger.handlers:
            #创建hander
            fh_stream = logging.StreamHandler()
            #设置级别
            fh_stream.setLevel(log_l[self.log_level])
            #设置输出格式
            formatter = logging.Formatter('%(asctime)s  %(name)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)

            #设置写入文件
            ft_file = logging.FileHandler(self.log_file)
            #设置级别
            ft_file.setLevel(log_l[self.log_level])
            #设置输出格式
            ft_file.setFormatter(formatter)

            #添加handers
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(ft_file)

#调用已经获取到logs文件路径方法
log_file = get_log_path()
#当前时间
curretr_time = datetime.datetime.now().strftime("%Y-%m-%d")
#调用已经获取yaml文件数据 log后缀名
log_extension = ConfigYaml().get_log_extension()

#把logs文件路径 和当前时间 以及后缀名 进行拼接
log_path = log_file+ "\\" + curretr_time+log_extension

#调用以及获取yaml文件 日志级别
log_level = ConfigYaml().get_log_level()
print(log_level)

#创建对外调用方法
def  my_log(log_name = __file__):
    return Logger(log_name =log_name,log_level = log_level,log_file =log_path).logger

if __name__ == "__main__":
    my_log("日志封装").debug("this is a debug")