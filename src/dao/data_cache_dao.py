# coding=utf-8
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

    def insert(self, dataCache) -> None:
        """
        插入一条数据
        :param dataCache: 数据
        """
        DataCache.create(code=dataCache.code, data=dataCache.data, crawling_rule_code=dataCache.crawling_rule_code)

    def delete(self, list) -> None:
        """
        删除已经同步的数据
        :param list: code 集合
        :return:
        """
        DataCache.delete().where(DataCache.code in list).execute()


if __name__ == '__main__':
    l = DataCacheDao().list()
    for i in l:
        print(i.code, i.data, i.crawling_rule_code)

    DataCacheDao().delete([1, 2])
