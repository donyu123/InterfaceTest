# -*- coding: utf-8 -*-
from  utils.ExcelUtil import ExcelReader
from  common.ExcelConfig import ExcelConfig
class Data:

    #初始化 调用excel工具类 获取结果
    def  __init__(self,excel_file,sheet_by):
       self.excelreader =ExcelReader(excel_file,sheet_by)

    #根据excel文档 是否运行 字段  查找用例
    def get_run_data(self):
        run_list = list()
        for lint in self.excelreader.data():
            if lint[ExcelConfig().is_run] =="y":
                #存到列表内
                run_list.append(lint)
        return run_list

    #查找全部测试用例
    def get_run_list(self):
        run_list = list()
        for lint in self.excelreader.data():
                run_list.append(lint)
        return run_list

    #查找全部用例  获取到前置条件测试用例 前置条件
    def get_run_pre(self,pre):
        run_list =self.get_run_list()
        for line in  run_list:
            if pre in dict(line).values():
                return line
        return None

# if __name__ == "__main__":
#     data_init = Data("../data/testdata.xlsx", "美多商城接口测试")
#     re=data_init.get_run_data()
#     data=data_init.get_run_pre(ExcelConfig().pre_exec)
#
#
#
#
#     print(re)
#     print(data)