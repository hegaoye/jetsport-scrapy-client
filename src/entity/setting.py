from peewee import CharField

from src.entity.base_model import BaseModel


class Setting(BaseModel):
    """
    设置 实体
    """
    key = CharField()
    value = CharField()

    class Meta:
        order_by = ('key',)
        db_table = 'task_pool'
