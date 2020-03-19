from peewee import PrimaryKeyField, TextField

from src.entity.base_model import BaseModel


class ApiTemplate(BaseModel):
    """
    提交接口的参数模板
    """
    api_code = PrimaryKeyField()
    args_template = TextField()

    class Meta:
        order_by = ('api_code',)
        db_table = 'api_template'
