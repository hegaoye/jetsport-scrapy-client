# coding=utf-8
from peewee import PrimaryKeyField, CharField, IntegerField

from src.entity.base_model import BaseModel


class Commands(BaseModel):
    """
    爬虫指令实体
    """
    code = PrimaryKeyField()
    command = CharField(max_length=64)
    type = CharField(max_length=16)
    order = IntegerField()
    state = CharField(max_length=16)


if __name__ == '__main__':
    Commands.create_table()
