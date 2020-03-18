# coding=utf-8
import datetime
import threading
import time

from src.base.log4py import logger

"""
仅用于 拉取服务器端的控制命令检测
"""
class PullCommandThread(threading.Thread):
    def __init__(self):
        pass
