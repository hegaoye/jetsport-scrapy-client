# coding=utf-8
import datetime


def getYesterday() -> str:
    """
    获取昨天
    :return: 昨天
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return str(yesterday)


if __name__ == '__main__':
    print(getYesterday())
