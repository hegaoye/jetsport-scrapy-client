from peewee import PrimaryKeyField, CharField, IntegerField, TextField

from src.entity.base_model import BaseModel


class TaskPool(BaseModel):
    """
    映射 task_pool 表的实体类
    """
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
