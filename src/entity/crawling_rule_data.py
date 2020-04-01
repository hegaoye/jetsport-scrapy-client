# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField

from src.entity.base_model import BaseModel


class CrawlingRuleData(BaseModel):
    """
    临时规则数据
    """
    id = PrimaryKeyField()
    code = CharField(max_length=64, null=True)
    pre_id = CharField(max_length=64, null=True)
    parameter_code = CharField(max_length=64, null=True)
    crawling_rule_code = CharField(max_length=64)
    parameter_name = CharField(max_length=64, null=True)
    value = TextField()

    class Meta:
        order_by = ('id',)
        db_table = 'crawling_rule_data'


if __name__ == '__main__':
    CrawlingRuleData.create_table()
