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


class BugFactoryThread(threading.Thread, Singleton):
    """
    虫子工厂，用于检测新的任务，并创建新的虫子出来，执行任务规则
    """

    def __init__(self):
        self.taskPoolDao = TaskPoolDao()
        self.crawlingRuleDao = CrawlingRuleDao()
        self.settingDao = SettingDao()
        self.list = []

    def run(self):
        """
        启动工厂
        """
        self.__factory()

    def __factory(self) -> None:
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
                    # 2.分配任务给虫子进行工作 todo 增加爬虫存活率检测，应将虫子放到集合中，并判断状态
                    bug = BugThread(crawlingRule)
                    bug.start()

                    bug_dict = {taskPool.code: bug}
                    self.list.append(bug_dict)

                    # 3.修改任务为工作中状态
                    self.taskPoolDao.updateStateByCode(taskPool.code, TaskPoolStateEnum.Working.name)

            time.sleep(factoryProduceFrequce)

            # 检查虫子是否还活着
            self.__check_alive_bugs()

    def __check_alive_bugs(self):
        """
        检查虫子是否还活着，如果死了就将任务重新打开交给新的虫子
        1.查询所有的任务池
        2.遍历生产的虫子集合，判断虫子状态
        3.移除死了的虫子
        """
        task_list = self.taskPoolDao.listByState(TaskPoolStateEnum.Working.name)
        if task_list.__sizeof__() > 0 and self.list.__sizeof__() > 0:
            dead_bug_list = []
            for task in task_list:
                for bug_dict in self.list:
                    bug = bug_dict[task.code]
                    if not bug:
                        self.taskPoolDao.updateStateByCode(task.code, TaskPoolStateEnum.Enable.name)
                    elif bug and not bug.is_alive():
                        self.taskPoolDao.updateStateByCode(task.code, TaskPoolStateEnum.Enable.name)
                        dead_bug_list.append(bug_dict)
            # 移除 死了的虫子
            self.list.remove(dead_bug_list)
