from src.service.base_service import BaseService


class SettingService(BaseService):
    def loadValue(self, key):
        """
        加载一个值
        :param key: 主键
        :return: 值
        """
        return self.settingDao.loadValue(key)

    def save(self, key, value) -> None:
        """
        插入一条设置
        :param key: key枚举
        :param value: 值
        """
        self.settingDao.insert(key, value)
