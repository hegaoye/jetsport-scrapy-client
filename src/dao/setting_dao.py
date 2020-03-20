# coding=utf-8
from src.base.singleton import Singleton
from src.entity.setting import Setting


class SettingDao(Singleton):
    """
    设置 dao层
    """

    def load(self, key) -> Setting:
        """
        加载设置
        :param key: 枚举键
        :return: Setting
        """
        return Setting.get(Setting.key == key)

    def loadValue(self, key):
        """
        加载一个值
        :param key: 主键
        :return: 值
        """
        return self.load(key).value

    def insert(self, key, value) -> None:
        """
        插入一条设置
        :param key_enum: key枚举
        :param value: 值
        """
        Setting.create(key=key, value=value)
