from enum import Enum


class CommandTypeEnum(Enum):
    """
    指令类型:开关 On_Off,定时 Timer,时间频率 Frequency
    """
    On_Off = "开关"
    Timer = "定时"
    Frequency = "时间频率"

