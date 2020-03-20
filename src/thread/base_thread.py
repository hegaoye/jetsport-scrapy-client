import threading

from src.service.setting_service import SettingService


class BaseTread(threading.Thread):
    """
    多线程基础类，用于初始化一些通用内容
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.settingService = SettingService()
