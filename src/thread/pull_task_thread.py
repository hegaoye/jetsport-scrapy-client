# coding=utf-8
import threading
import time

from src.base.enum.setting_key_enum import SettingKeyEnum
from src.base.log4py import logger
from src.dao.setting_dao import SettingDao
from src.service.pull_task_serivce import PullTaskService

"""
用于检测服务器端分发新任务
"""


class PullTaskThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.settingDao = SettingDao()
        self.pullTaskService = PullTaskService()

    def run(self):
        """
        进行任务检测每N分钟执行一次
        :return:
        """
        pullTaskFrequceSecond = int(self.settingDao.loadValue(SettingKeyEnum.PullTaskFrequce.name))
        while True:
            try:
                # 拉取任务
                self.pullTaskService.pull()
            except Exception as e:
                logger.error(e)

            # 自动休眠 n 秒
            time.sleep(pullTaskFrequceSecond)
