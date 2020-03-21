# coding=utf-8
from peewee import PrimaryKeyField, CharField, IntegerField

from src.entity.base_model import BaseModel


class CrawlingRule(BaseModel):
    """
    爬虫规则
    """
    # 编码
    code = PrimaryKeyField()
    # 接口编码
    api_code = CharField(max_length=64)
    # 获取值方法
    get_value_method = CharField(max_length=16)
    # 接口属性
    api_field = CharField(max_length=64)
    # 属性类型
    field_type = CharField(max_length=16)
    # 值类型
    value_type = CharField(max_length=16)
    # 爬取结构类型
    result_type = CharField(max_length=16)
    # xpath
    xpath = CharField(max_length=256)
    # xpath 类型
    xpath_type = CharField(max_length=16)
    # 操作方式
    opt = CharField(max_length=16)
    # 入口url
    access_url = CharField(max_length=256)
    # 上级编码
    pre_code = CharField(max_length=64)
    # 爬虫服务器的接口地址
    api_url = CharField(max_length=256)
    # 取值属性名
    html_attr = CharField(max_length=128)
    # 爬取频率
    frequce = IntegerField()
    # 排序
    ordinal = IntegerField()

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_rule'


if __name__ == '__main__':
    CrawlingRule.create_table()
