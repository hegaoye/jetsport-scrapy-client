# coding=utf-8
from peewee import PrimaryKeyField, CharField, IntegerField, TextField

from src.entity.base_model import BaseModel


class TaskPool(BaseModel):
    """
    映射 task_pool 表的实体类
    """
    code = PrimaryKeyField()
    crawling_rule_code = CharField(max_length=64)
    state = CharField(max_length=16)
    ordinal = IntegerField()
    push_frequce = IntegerField()
    task_url = CharField(max_length=256)
    header = TextField()

    class Meta:
        order_by = ('ordinal',)
        db_table = 'task_pool'


if __name__ == '__main__':
    TaskPool.create_table()
