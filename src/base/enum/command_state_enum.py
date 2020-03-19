# coding=utf-8
from enum import Enum


class CommandStateEnum(Enum):
    """
    状态:初始化 Init,执行中 Doing,已执行 Executed
    """
    Init = "初始化"
    Doing = "执行中"
    Executed = "已执行"
