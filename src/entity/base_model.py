from peewee import Model, SqliteDatabase

from settings import DATABASE_PATH

db = SqliteDatabase(DATABASE_PATH)

"""
基础 实体类基础
"""


class BaseModel(Model):
    class Meta:
        database = db
