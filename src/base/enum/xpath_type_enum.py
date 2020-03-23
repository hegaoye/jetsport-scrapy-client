# coding=utf-8
from enum import Enum


class XpathTypeEnum(Enum):
    """
    xpath类型：集合 List，点击 Click，链接 Link，元素 Element，文本 Text，图像 Image，视频 Video，声音 Audio
    """
    List = "集合"
    Click = "点击"
    Link = "链接"
    Element = "元素"
    Text = "文本"
    Image = "图片"
    Video = "视频"
    Audio = "声音"
