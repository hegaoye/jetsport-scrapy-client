# coding=utf-8
from src.base.singleton import Singleton
from src.entity.task_pool import TaskPool


class TaskPoolDao(Singleton):
    """
    任务池dao
    """

    def load(self, state) -> TaskPool:
        """
        根据状态加载一个任务
        :param state: 状态机
        :return: TaskPool
        """
        list = TaskPool.select().where(TaskPool.state == state).order_by(TaskPool.ordinal.asc())
        if list and len(list) > 0:
            return list.get()
        else:
            return None

    def load_by_crawling_rule_code(self, crawling_rule_code) -> TaskPool:
        """
        根据 爬取规则编码查询任务
        :param crawling_rule_code: 爬虫规则编码
        :return: TaskPool
        """
        return TaskPool.get(TaskPool.crawling_rule_code == crawling_rule_code)

    def list_by_state(self, state) -> list:
        """
        根据状态查询任务的集合
        :param state: 状态
        :return: list
        """
        return TaskPool.select().where(TaskPool.state == state)

    def update_state_by_code(self, code, state):
        """
        根据code 更新 状态
        :param code:  code 编码
        :param state:  具体状态
        """
        TaskPool.update(state=state).where(TaskPool.code == code).execute()

    def insert(self, taskPool) -> None:
        """
         保存任务到任务池中
        :param taskPool: 任务池数据
        """
        TaskPool.create(code=taskPool.code, crawling_rule_code=taskPool.crawling_rule_code,
                        state=taskPool.state, ordinal=taskPool.ordinal, push_frequce=taskPool.push_frequce,
                        task_url=taskPool.task_url, header=taskPool.header)
