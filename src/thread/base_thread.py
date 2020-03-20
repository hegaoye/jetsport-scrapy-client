import threading

from src.service.setting_service import SettingService


class BaseTread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.settingService = SettingService()
