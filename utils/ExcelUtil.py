import  xlrd
import  os
from  utils.LogUtil import my_log

class   ExcelReader :

    #初始化方法 excel路径 和shheet的名称
    def __init__(self,excel_file,sheet_by):
        self.log = my_log("日志封装")
        #判断路径里面是否有用例文档，有就读取
        if os.path.exists(excel_file):
            self.excel_flie = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise  FileNotFoundError("文件不存在")

    #读取sheet
    def data(self):

        #创建workbook对象
        workbook = xlrd.open_workbook(self.excel_flie)

        #判断读取的方式
        if type(self.sheet_by) not in [str,int]:
            self.log.error("读取方式错误,索引或名称方式进行读取")
        elif type(self.sheet_by) == int :
             sheet = workbook.sheet_by_index(self.sheet_by)

       #名称方式
        elif type(self.sheet_by) == str:
            sheet = workbook.sheet_by_name(self.sheet_by)

        #读取sheet内容 读取首行
        title = sheet.row_values(0)
        # print(title)

        #遍历测试行 与第0行组成字典
        for col in range(1,sheet.nrows):
            col_value = sheet.row_values(col)
            # print(col_value)
            # data_dict= dict(zip(title,col_value))
            self._data.append(dict(zip(title,col_value)))
        return  self._data

# if __name__ == "__main__":
#     reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
#     print(reader.data())