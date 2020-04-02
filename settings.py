# coding=utf-8
"""
配置上下文 文件
注意配置文件变量必须大写否则错误
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库配置
DATABASE_PATH = os.path.join(_basedir, 'data.db')
LOGGIN_CONF = os.path.join(_basedir, 'logging.conf')
LOGGIN_FILE = os.path.join(_basedir, 'app.log')
BROWSER_PATH = os.path.join(_basedir, 'chromedriver.exe')
# BROWSER_PATH=os.path.join(_basedir,'chromedriver_mac')

del os
