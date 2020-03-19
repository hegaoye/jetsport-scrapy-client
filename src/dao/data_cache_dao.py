# coding=utf-8

from src.base.databasetools import Sqlite3Tools


class DataCacheDao:
    """
    数据缓存dao
    """

    def __init__(self):
        self.db = Sqlite3Tools()
