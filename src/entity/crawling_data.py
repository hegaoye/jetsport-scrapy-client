from peewee import PrimaryKeyField, CharField, TextField

from src.entity.base_model import BaseModel


class CrawlingData(BaseModel):
    id = PrimaryKeyField()
    crawling_code = CharField(max_length=64)
    value = TextField()
    data_type = CharField(max_length=16)
    pre_code = CharField(max_length=64)

    class Meta:
        order_by = ('code',)
        db_table = 'crawling_data'


if __name__ == '__main__':
    CrawlingData.create_table()
