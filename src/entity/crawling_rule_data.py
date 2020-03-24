# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField, IntegerField

from src.entity.base_model import BaseModel


class CrawlingRuleData(BaseModel):
    """
    临时规则数据
    """
    id = PrimaryKeyField()
    pre_id = IntegerField()
    parameter_code = CharField(max_length=64)
    crawling_rule_code = CharField(max_length=64)
    parameter_name = CharField(max_length=64)
    value = TextField()

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_rule_data'


if __name__ == '__main__':
    CrawlingRuleData.create_table()
