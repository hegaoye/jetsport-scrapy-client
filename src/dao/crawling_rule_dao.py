# coding=utf-8
from src.entity.crawling_rule import CrawlingRule


class CrawlingRuleDao:
    """
    爬取规则Dao
    """

    def insert(self, crawlingRule) -> None:
        CrawlingRule.create()

    def load(self, code) -> CrawlingRule:
        """
        加载一个
        :param code:
        :return:
        """
        return CrawlingRule.get(CrawlingRule.code == code)
