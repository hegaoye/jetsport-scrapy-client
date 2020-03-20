# coding=utf-8
import time

from src.base.enum.setting_key_enum import SettingKeyEnum
from src.base.log4py import logger
from src.service.task_serivce import TaskService
from src.thread.base_thread import BaseTread


class PullTaskThread(BaseTread):
    """
    用于检测服务器端分发新任务
    """

    def __init__(self):
        self.pullTaskService = TaskService()

    def run(self) -> None:
        """
        进行任务检测每N分钟执行一次
        :return:
        """
        pullTaskFrequceSecond = int(self.settingService.loadValue(SettingKeyEnum.PullTaskFrequce.name))
        while True:
            try:
                # 拉取任务
                self.pullTaskService.pull()
            except Exception as e:
                logger.error(e)

            # 自动休眠 n 秒
            time.sleep(pullTaskFrequceSecond)
