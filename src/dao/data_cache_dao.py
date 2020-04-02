# coding=utf-8
import json

from src.entity.data_cache import DataCache


class DataCacheDao:
    """
    数据缓存dao
    """

    def list(self) -> list:
        """
        查询数据的集合
        :return: list
        """
        return DataCache.select()

    def insert(self, dataCache) -> int:
        """
        插入一条数据
        :param dataCache: 数据
        """
        return DataCache.insert(api_code=dataCache.api_code, data=dataCache.data).execute()

    def delete(self, code_list) -> None:
        """
        删除已经同步的数据
        :param code_list: code 集合
        :return:
        """
        DataCache.delete().where(DataCache.code in code_list).execute()


if __name__ == '__main__':
    l = DataCacheDao().list()
    for i in l:
        print(i.code, i.data, i.crawling_rule_code)

    ls = []
    data = {}
    data["name"] = "a"
    data["age"] = 19
    ls.append(data)

    print(json.dumps(ls))
