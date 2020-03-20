from peewee import PrimaryKeyField, CharField, IntegerField

from src.entity.base_model import BaseModel


class Commands(BaseModel):
    """
    爬虫指令实体
    """
    code = PrimaryKeyField()
    command = CharField()
    type = CharField()
    order = IntegerField()
    state = CharField()
