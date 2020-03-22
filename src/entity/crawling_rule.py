# coding=utf-8
from peewee import PrimaryKeyField, CharField, IntegerField

from src.entity.base_model import BaseModel


class CrawlingRule(BaseModel):
    """
    爬虫规则
    """
    # 编码
    code = PrimaryKeyField()
    # 上级编码
    pre_code = CharField(max_length=64)
    # 接口编码
    api_code = CharField(max_length=64)
    # 参数编码
    parameter_code = CharField(max_length=64)
    # xpath
    xpath = CharField(max_length=256)
    # xpath 类型
    xpath_type = CharField(max_length=16)
    # 获取值方法
    get_value_type = CharField(max_length=16)
    # 取值属性名
    html_attr = CharField(max_length=128)
    # 入口url
    access_url = CharField(max_length=256)
    # 爬取频率
    frequce = IntegerField()
    # 是否是参数规则 Y 是，参数规则则映射接口的参数 , N 否，不是参数规则，则仅用于打开网址，或者点击操作等规则
    is_parameter = CharField(max_length=8)
    # 排序
    ordinal = IntegerField()

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_rule'


if __name__ == '__main__':
    CrawlingRule.create_table()
