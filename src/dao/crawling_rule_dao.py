# coding=utf-8
from src.base.singleton import Singleton
from src.entity.crawling_rule import CrawlingRule


class CrawlingRuleDao(Singleton):
    """
    爬取规则Dao
    """

    def insert(self, crawlingRule) -> None:
        CrawlingRule.create()

    def load(self, code) -> CrawlingRule:
        """
        加载一条爬虫规则
        :param code:
        :return:
        """
        return CrawlingRule.get(CrawlingRule.code == code)
