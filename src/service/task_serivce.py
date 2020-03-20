# coding=utf-8
from src.base import http
from src.base.enum.setting_key_enum import SettingKeyEnum
from src.dao.task_pool_dao import TaskPoolDao
from src.entity.task_pool import TaskPool
from src.service.base_service import BaseService


class TaskService(BaseService):
    """
    拉取任务检测接口
    """

    def __init__(self):
        # 获取设置类，获取拉取地址和host等
        self.taskPoolDao = TaskPoolDao()

    def load(self, state) -> TaskPool:
        """
        根据状态加载一个任务
        :param state: 状态机
        :return: TaskPool
        """
        return self.taskPoolDao.load(state)

    def updateStateByCode(self, code, state):
        """
        根据code 更新 状态
        :param code:  code 编码
        :param state:  具体状态
        """
        self.taskPoolDao.updateStateByCode(code, state)

    def listByState(self, state) -> list:
        """
        根据状态查询任务的集合
        :param state: 状态
        :return: list
        """
        return self.taskPoolDao.listByState(state)

    def pull(self):
        """
        拉取任务检测
        1.获取拉取任务的请求地址
        2.拉取任务
        3.存储任务到任务列表
        :return:
        """
        # 1.获取拉取任务的请求地址
        pull_task_url = self.settingDao.loadValue(SettingKeyEnum.PullTaskUrl.name)

        # 2.拉取任务
        r = http.get(pull_task_url)
        if not r.success:
            return
        else:
            # 3.#存储任务到任务列表
            taskPool = TaskPool()
            # todo 获取数据进行保存
            self.taskPoolDao.insert(taskPool)

    def push(self):
        pass
