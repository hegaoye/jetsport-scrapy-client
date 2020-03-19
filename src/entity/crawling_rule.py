from peewee import PrimaryKeyField, CharField, IntegerField

from src.entity.base_model import BaseModel


class CrawlingRule(BaseModel):
    """
    爬虫规则
    """
    code = PrimaryKeyField()
    api_code = CharField()
    get_value_method = CharField()
    api_field = CharField()
    field_type = CharField()
    value_type = CharField()
    result_type = CharField()
    frequce = IntegerField()
    xpath = CharField()
    sub_xpath = CharField()
    sub_xpath_relative = CharField()
    sub_label = CharField()
    sub_label_class = CharField()
    opt = CharField()
    access_url = CharField()
    target_code = CharField()
    pre_code = CharField()
    api_url = CharField()

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_rule'
