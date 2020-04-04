# coding=utf-8
from peewee import PrimaryKeyField, TextField

from src.entity.base_model import BaseModel


class ApiTemplate(BaseModel):
    """
    提交接口的参数模板
    """
    api_code = PrimaryKeyField(null=True)
    args_template = TextField(null=True)

    class Meta:
        order_by = ('api_code',)
        db_table = 'api_template'
