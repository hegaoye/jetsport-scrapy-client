# coding=utf-8

from src.base.databasetools import Sqlite3Tools


class ApiTemplateDao:
    """
    接口参数模板Dao
    """

    def __init__(self):
        self.db = Sqlite3Tools()
