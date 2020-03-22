# coding=utf-8
from src.base.singleton import Singleton
from src.entity.parameter import Parameter


class ParameterDao(Singleton):
    """
    api parameter dao
    """

    def load(self, code) -> Parameter:
        return Parameter.get(Parameter.code == code)

    def list(self, api_code) -> list:
        return Parameter.select().where(Parameter.api_code == api_code)

    def insert(self, parameter) -> None:
        Parameter.create(code=parameter.code, api_code=parameter.api_code, name=parameter.name, type=parameter.type)
