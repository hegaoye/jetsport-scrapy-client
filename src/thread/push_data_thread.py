# coding=utf-8
from time import sleep

from src.base.enum.setting_key_enum import SettingKeyEnum
from src.service.data_cache_service import DataCacheService
from src.thread.base_thread import BaseTread


class PushDataThread(BaseTread):
    """
    仅用于 批量推送本地数据到服务器
    """

    def __init__(self):
        self.dataCacheService = DataCacheService()

    def run(self) -> None:
        push_data_cache_frequce = self.settingService.load_value(SettingKeyEnum.PushDataCacheFrequce.name)
        while True:
            self.__push()
            sleep(push_data_cache_frequce)

    def __push(self) -> None:
        """
        推送数据到服务器
        """
        try:
            # 推送数据到服务端
            self.dataCacheService.push()
        except:
            pass
