# coding=utf-8

from src.service.data_cache_service import DataCacheService
from src.thread.base_thread import BaseTread


class PushDataThread(BaseTread):
    """
    仅用于 批量推送本地数据到服务器
    """

    def __init__(self, api):
        self.dataCacheService = DataCacheService()
        self.api = api

    def run(self) -> None:
        self.__push(self.api)

    def __push(self, api) -> None:
        """
        推送数据到服务器
        """
        try:
            # 推送数据到服务端
            self.dataCacheService.push(api)
        except:
            pass
