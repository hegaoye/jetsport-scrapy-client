from peewee import CharField, PrimaryKeyField

from src.entity.base_model import BaseModel


class Setting(BaseModel):
    """
    设置 实体
    """
    key = PrimaryKeyField()
    value = CharField()

    class Meta:
        order_by = ('key',)
        db_table = 'setting'
