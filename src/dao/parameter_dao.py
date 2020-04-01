# coding=utf-8
import uuid

from src.base.singleton import Singleton
from src.entity.parameter import Parameter


class ParameterDao(Singleton):
    """
    api parameter dao
    """

    def load(self, code) -> Parameter:
        return Parameter.get(Parameter.code == code)

    def list(self, api_code, is_root) -> list:
        return Parameter.select().where(Parameter.api_code == api_code, Parameter.is_root == is_root)

    def insert(self, parameter) -> None:
        Parameter.create(code=parameter.code, api_code=parameter.api_code, name=parameter.name, type=parameter.type)
