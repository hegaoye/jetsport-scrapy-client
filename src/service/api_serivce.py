# coding=utf-8
from src.dao.api_dao import ApiDao
from src.entity.api import Api
from src.service.base_service import BaseService


class ApiService(BaseService):
    def __init__(self):
        self.apiDao = ApiDao()

    def load(self, code) -> Api:
        return self.apiDao.load(code)
