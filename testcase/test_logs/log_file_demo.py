# -*- coding: utf-8 -*-
import  logging
#设置控制台名称

logger = logging.getLogger("日志")

#设置日志级别
logger.setLevel(logging.INFO)

#创建henader
fh_Stream = logging.StreamHandler()

#把日志信息写入指定文件
fh_file = logging.FileHandler("./test.log")

#设置日志级别
fh_Stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)

#设置输出格式
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')


#添加输出格式
fh_Stream.setFormatter(formatter)
fh_file.setFormatter(formatter)

#添加handers
logger.addHandler(fh_Stream)
logger.addHandler(fh_file)

logger.info("this is a info")
logger.debug("this is a debug")
logger.warning("this is a warning")