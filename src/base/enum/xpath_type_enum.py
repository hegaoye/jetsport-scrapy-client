# coding=utf-8
from enum import Enum


class XpathTypeEnum(Enum):
    Click = "点击"
    Link = "链接"
    Element = "元素"
    Text = "文本"
    Image = "图片"
    Video = "视频"
