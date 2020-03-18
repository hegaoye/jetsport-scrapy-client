from peewee import PrimaryKeyField, CharField, IntegerField, TextField

from src.entity.base_model import BaseModel

"""
映射 task_pool 表的实体类
"""


class TaskPool(BaseModel):
    code = PrimaryKeyField()
    crawling_rule_code = CharField()
    state = CharField()
    ordinal = IntegerField()
    push_frequce = IntegerField()
    task_url = CharField()
    header = TextField()

    class Meta:
        order_by = ('ordinal',)
        db_table = 'task_pool'

if __name__ == '__main__':
    t=TaskPool()
    t.code="aaa"
    print(t.code)