# -*- coding: utf-8 -*-
import  xlrd

#创建workbook对象
book = xlrd.open_workbook("testdata.xlsx")
#获取sheet名称
sheet = book.sheet_by_name("美多商城接口测试")
#获取行数 和列数
rows = sheet.nrows
cols = sheet.ncols

#读取每行内容
for i in range(rows):
    r_value = sheet.row_values(i)
    print(r_value)

#读取列内容
# for i in range(cols):
#     c_value = sheet.col_values(i)
#     print(c_value)