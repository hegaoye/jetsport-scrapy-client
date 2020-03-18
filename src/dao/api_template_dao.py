# coding=utf-8

from src.base.databasetools import Sqlite3Tools


class ApiTemplateDao:
    def __init__(self):
        self.db = Sqlite3Tools()

