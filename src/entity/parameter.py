# coding=utf-8
from peewee import PrimaryKeyField, TextField, CharField

from src.entity.base_model import BaseModel


class Parameter(BaseModel):
    """
    接口 参数
    """
    code = PrimaryKeyField()
    api_code = CharField(max_length=64)
    name = CharField(max_length=16)
    type = CharField(max_length=16)

    class Meta:
        order_by = ('code',)
        db_table = 'parameter'


if __name__ == '__main__':
    Parameter.create_table()
