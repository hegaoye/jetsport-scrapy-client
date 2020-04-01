# coding=utf-8
from src.base.singleton import Singleton
from src.entity.api import Api


class ApiDao(Singleton):
    """
    api 接口dao
    """

    def load(self, code) -> Api:
        return Api.get(Api.code == code)

    def list(self) -> list:
        return Api.select()

    def insert(self, api) -> None:
        Api.create(code=api.code, url=api.url, request_method=api.request_method, parameter_type=api.parameter_type)
