from src.base import http
from src.dao.crawling_rule_dao import CrawlingRuleDao
from src.dao.data_cache_dao import DataCacheDao
from src.dao.task_pool_dao import TaskPoolDao
from src.service.base_service import BaseService


class DataCacheService(BaseService):
    """
    缓存数据服务接口
    """

    def __init__(self):
        self.dataCacheDao = DataCacheDao()
        self.crawlingRuleDao = CrawlingRuleDao()
        self.taskPoolDao = TaskPoolDao()

    def save(self, dataCache) -> None:
        """
        保存一个数据到数据库
        :param dataCache: 爬取的数据
        """
        self.dataCacheDao.insert(dataCache)

    def push(self) -> bool:
        """
        推送数据到服务端
        1.查询所有的数据集合
        2.推送数据整合
        3.精准删除已经推送的数据
        :return: True/False
        """
        # 1.查询所有的数据集合
        list = self.dataCacheDao.list()
        data_cache_code_list = []
        if list and list.__sizeof__() > 0:
            for data_cache in list:
                crawling_rule = self.crawlingRuleDao.load_by_code(data_cache.crawling_rule_code)

                # 2.推送数据整合
                if crawling_rule:
                    url = crawling_rule.api_url
                    task_pool = self.taskPoolDao.load_by_crawling_rule_code(crawling_rule.code)

                    # 构造数据接口
                    data = {
                        "taskPoolCode": task_pool.code,
                        "crawlingRuleCode": crawling_rule.code,
                        "data": data_cache.data
                    }

                    # 推送数据
                    r = http.post(url, data)
                    if r.success:
                        data_cache_code_list.append(data_cache.code)

            # 3.精准删除已经推送的数据
            if data_cache_code_list.__sizeof__() > 0:
                self.dataCacheDao.delete(data_cache_code_list)
