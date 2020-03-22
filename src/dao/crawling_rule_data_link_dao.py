# coding=utf-8
from src.base.singleton import Singleton
from src.entity.crawling_rule_data import CrawlingRuleData
from src.entity.crawling_rule_data_link import CrawlingRuleDataLink


class CrawlingRuleDataLinkDao(Singleton):
    """
    api parameter dao
    """

    def load(self, id) -> CrawlingRuleDataLink:
        return CrawlingRuleDataLink.get(CrawlingRuleData.id == id)

    def list(self, crawling_rule_code) -> list:
        return CrawlingRuleDataLink.select().where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def delete(self, id) -> int:
        return CrawlingRuleDataLink.delete_by_id(id)

    def insert(self, crawlingRuleDataLink) -> None:
        CrawlingRuleDataLink.create(crawling_rule_code=crawlingRuleDataLink.crawling_rule_code,
                                    link=crawlingRuleDataLink.link)
