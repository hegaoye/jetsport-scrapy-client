# coding=utf-8

from src.base.databasetools import Sqlite3Tools


class CrawlingRuleDao:
    """
    爬取规则Dao
    """

    def __init__(self):
        self.db = Sqlite3Tools()
