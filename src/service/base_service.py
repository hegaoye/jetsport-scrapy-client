from src.base.singleton import Singleton
from src.dao.setting_dao import SettingDao


class BaseService(Singleton):
    """
    基础服务类
    """

    def __init__(self):
        self.settingDao = SettingDao()
