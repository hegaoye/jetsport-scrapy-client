# coding=utf-8
from enum import Enum


class ParameterTypeEnum(Enum):
    """
    参数类型：Map,Field,Uri
    """
    List = "List"
    Map = "Map"
    Field = "Field"
    Uri = "Uri"
