# coding=utf-8
from src.dao.parameter_dao import ParameterDao
from src.entity.parameter import Parameter
from src.service.base_service import BaseService


class ParameterService(BaseService):
    def __init__(self):
        self.parameterDao = ParameterDao()

    def load(self, code) -> Parameter:
        return self.parameterDao.load(code)

    def list(self, api_code, is_root) -> list:
        return self.parameterDao.list(api_code, is_root)
