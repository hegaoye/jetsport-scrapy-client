from enum import Enum

"""
可作业 Enable,作业中 Working,停止作业 Stop_Task,报错暂停 Stop_Error
"""


class TaskPoolStateEnum(Enum):
    Enable = "可作业"
    Working = "作业中"
    Stop_Task = "停止作业"
    Stop_Error = "报错暂停"
