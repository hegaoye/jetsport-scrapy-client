# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField

from src.entity.base_model import BaseModel


class DataCache(BaseModel):
    """
    数据缓存实体
    """
    code = PrimaryKeyField()
    data = TextField()
    crawling_rule_code = CharField()

    class Meta:
        order_by = ('code',)
        db_table = 'data_cache'
