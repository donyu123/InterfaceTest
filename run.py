# -*- coding: utf-8 -*-
from  config import Conf_File
import pytest
import os

if __name__ == '__main__':

    # 日志报告json文件123
    report_path = Conf_File.get_report_path() + os.sep + "result"
    # 日志报告
    report_path_html = Conf_File.get_report_path() + os.sep + "html"
    # 执行请求 并且生成报告json文件
    pytest.main(["-s","--alluredir", report_path])