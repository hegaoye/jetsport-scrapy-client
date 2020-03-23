# coding=utf-8
from peewee import PrimaryKeyField, CharField

from src.entity.base_model import BaseModel


class Parameter(BaseModel):
    """
    接口 参数
    """
    code = PrimaryKeyField()
    pre_code = CharField(max_length=64)
    api_code = CharField(max_length=64)
    name = CharField(max_length=16)
    field_type = CharField(max_length=16)
    parameter_type = CharField(max_length=16)

    class Meta:
        order_by = ('code',)
        db_table = 'parameter'


if __name__ == '__main__':
    Parameter.create_table()
