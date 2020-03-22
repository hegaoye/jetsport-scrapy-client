from enum import Enum


class GetValueTypeEnum(Enum):
    """
    取值类型  文本 Text,属性 Attribute,下载 Download
    """
    # 文本
    Text = "Text"
    # 属性
    Attribute = "Attribute"
    # 下载
    Download = "Download"
