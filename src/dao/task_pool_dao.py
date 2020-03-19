# coding=utf-8
from src.entity.task_pool import TaskPool


class TaskPoolDao:
    """
    任务池dao
    """

    def insert(self, taskPool):
        """
         保存任务到任务池中
        :param taskPool: 任务池数据
        """
        TaskPool.create(code=taskPool.code, crawling_rule_code=taskPool.crawling_rule_code,
                        state=taskPool.state, ordinal=taskPool.ordinal, push_frequce=taskPool.push_frequce,
                        task_url=taskPool.task_url, header=taskPool.header)


if __name__ == '__main__':
    t = TaskPool()
    t.code = "2222"
    # TaskPoolDao().insert(t)
    tt = TaskPool.get(code="aaa")
    print(tt.code, tt.state, tt.header)
    ts = TaskPool.select().where(TaskPool.code != None)
    for tobj in ts:
        print(tobj.code, tobj.state)
