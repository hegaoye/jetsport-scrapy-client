# coding=utf-8
from src.base.databasetools import Sqlite3Tools

"""
设置 dao层
"""


class SettingDao:
    def __init__(self):
        self.db = Sqlite3Tools()

    def load(self, key_enum):
        """
        加载设置
        :param key_enum: 枚举键
        :return:
        """
        sql = 'select * from setting where key="' + str(key_enum.value) + '"'
        result = self.db.load(sql)
        if result:
            return {"key": result[0], "value": result[1]}
        return None

    def update(self, key_enum, value):
        """
        更新设置值
        :param key_enum:键枚举
        :param value:值
        """
        sql = 'update setting set value="' + str(value) + '"  where key="' + key_enum.value + '"'
        self.db.update(sql)

    def insert(self, key_enum, value):
        """
        插入一条设置
        :param key_enum: key枚举
        :param value: 值
        """
        sql = "insert into setting(key,value) " \
              "VALUES ('" + str(key_enum.value) + "','" + str(value) + "') "
        self.db.insert(sql)
