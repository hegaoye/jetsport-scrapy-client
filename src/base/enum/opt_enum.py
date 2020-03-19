# coding=utf-8
from enum import Enum


class OptEnum(Enum):
    """
    操作: 点击爬取 Click_Crawling，直接爬取 Crawling
    """
    Click_Crawling = "点击爬取"
    Crawling = "直接爬取"
