# coding=utf-8
from enum import Enum


class ParameterTypeEnum(Enum):
    """
    参数类型：List,Map,Uri
    """
    List = "List"
    Map = "Map"
    Uri = "Uri"
