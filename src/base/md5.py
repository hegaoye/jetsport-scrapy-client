# coding=utf-8
import hashlib


def md5(text) -> str:
    """
    md5 加密
    :param text: 铭文文本
    :return: 字符串
    """
    m2 = hashlib.md5()
    m2.update(text.encode(encoding='utf-8'))
    return m2.hexdigest()
