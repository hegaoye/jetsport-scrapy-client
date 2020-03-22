# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField

from src.entity.base_model import BaseModel


class DataCache(BaseModel):
    """
    数据缓存实体
    """
    id = PrimaryKeyField()
    crawling_rule_code = CharField(max_length=64)
    task_code = CharField(max_length=64)
    api_code = CharField(max_length=64)
    data = TextField()

    class Meta:
        order_by = ('id',)
        db_table = 'data_cache'


if __name__ == '__main__':
    DataCache.create_table()
