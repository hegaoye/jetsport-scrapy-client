# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField

from src.entity.base_model import BaseModel


class CrawlingRuleDataLink(BaseModel):
    """
    爬虫规则中间链接
    """
    id = PrimaryKeyField()
    crawling_rule_code = CharField(max_length=64)
    link = TextField()

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_rule_data_link'


if __name__ == '__main__':
    CrawlingRuleDataLink.create_table()
