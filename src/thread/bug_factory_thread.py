# coding=utf-8
import threading
import time

from src.base.enum.setting_key_enum import SettingKeyEnum
from src.base.enum.task_pool_state_enum import TaskPoolStateEnum
from src.base.singleton import Singleton
from src.dao.crawling_rule_dao import CrawlingRuleDao
from src.dao.setting_dao import SettingDao
from src.dao.task_pool_dao import TaskPoolDao
from src.thread.bug_thread import BugThread

"""
虫子工厂，用于检测新的任务，并创建新的虫子出来，执行任务规则
"""


class BugFactoryThread(threading.Thread, Singleton):
    def __init__(self):
        self.taskPoolDao = TaskPoolDao()
        self.crawlingRuleDao = CrawlingRuleDao()
        self.settingDao = SettingDao()

    def run(self):
        pass

    def factory(self) -> None:
        """
        生产虫子的工厂方法
        1.获取任务池中待分配的任务
        2.分配任务给虫子进行工作
        3.修改任务为工作中状态
        """
        # 工厂制造频率
        factoryProduceFrequce = int(self.settingDao.loadValue(SettingKeyEnum.FactoryProduceFrequce))

        while True:
            # 1.获取任务池中待分配的任务
            taskPool = self.taskPoolDao.load(TaskPoolStateEnum.Enable.name)
            if taskPool:

                crawlingRule = self.crawlingRuleDao.load(taskPool.crawling_rule_code)
                if crawlingRule:
                    # 2.分配任务给虫子进行工作
                    BugThread(crawlingRule).start()

                    # 3.修改任务为工作中状态
                    self.taskPoolDao.updateStateByCode(taskPool.code, TaskPoolStateEnum.Working.name)
            else:
                time.sleep(factoryProduceFrequce)
