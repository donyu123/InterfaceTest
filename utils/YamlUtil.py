# -*- coding: utf-8 -*-
import  os
import  yaml

class YamlReader:
    def __init__(self,yamlf):

        #判断yaml文件是否存在
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise  FileNotFoundError("文件不存在 未找到")
        self._data = None
        self._data_all = None

    #读取单个文件
    def  data (self):
        #判断文件是否是第一次打开 读取yaml文档 如果不是返回之前的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
        return  self._data

    #读取多个文件 需要注意 是返回多个文档 用list列表包住 否则返回是 类的地址值
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all

# if  __name__  =="__main__":
#     ym=YamlReader("D:\pycode\config\conf.yml")
#     print(ym.data())