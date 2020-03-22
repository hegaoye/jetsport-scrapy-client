# coding=utf-8
from peewee import PrimaryKeyField, CharField

from src.entity.base_model import BaseModel


class Api(BaseModel):
    """
    接口
    """
    code = PrimaryKeyField()
    url = CharField(max_length=128)
    request_method = CharField(max_length=16)
    parameter_type = CharField(max_length=16)

    class Meta:
        order_by = ('code',)
        db_table = 'api'


if __name__ == '__main__':
    Api.create_table()
