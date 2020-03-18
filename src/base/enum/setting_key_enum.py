from enum import Enum, unique

"""
设置表映射 key 枚举值 （仅用于设置表中的枚举）
"""


@unique
class SettingKeyEnum(Enum):
    """
    主机地址
    """
    Host = "Host"

    """
    请求秘钥和key
    """
    APP_Key = "APP_Key"
    APP_Secret = "APP_Secret"

    """
     拉取任务检测间隔的时间 key
    """
    PullTaskFrequce = "PullTaskFrequce"

    """
    拉取任务的地址
    """
    PullTaskUrl = "PullTaskUrl"
