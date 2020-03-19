# coding=utf-8
from src.base.databasetools import Sqlite3Tools
from src.entity.setting import Setting


class SettingDao:
    """
    设置 dao层
    """

    def __init__(self):
        self.db = Sqlite3Tools()

    def load(self, key):
        """
        加载设置
        :param key: 枚举键
        :return:
        """
        return Setting.get(Setting.key == key)

    def loadValue(self, key):
        """
        加载一个值
        :param key: 主键
        :return:
        """
        return self.load(key).value

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
