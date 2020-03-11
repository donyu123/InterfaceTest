# -*- coding: utf-8 -*-
import  logging
#1、导入Logging包
import logging
#2、设置配置信息
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#3、定义日志名称getlogger
logger = logging.getLogger("log_demo")
#4、info,debug
logger.debug("debug")
logger.info("info")

logger.warning("warning")

