# coding=utf-8

from src.entity.task_pool import TaskPool


class TaskPoolDao:

    def insert(self, taskPool):
        TaskPool.create(code=taskPool.code, crawling_rule_code=taskPool.crawling_rule_code,
                        state=taskPool.state, ordinal=taskPool.ordinal, push_frequce=taskPool.push_frequce,
                        task_url=taskPool.task_url, header=taskPool.header)


if __name__ == '__main__':
    t = TaskPool()
    t.code = "1111"
    TaskPoolDao().insert(t)
