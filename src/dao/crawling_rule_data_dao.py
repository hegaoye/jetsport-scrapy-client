# coding=utf-8
from src.base.singleton import Singleton
from src.entity.crawling_rule_data import CrawlingRuleData


class CrawlingRuleDataDao(Singleton):
    """
    api parameter dao
    """

    def load(self, id) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.id == id)

    def load(self, pre_id, crawling_rule_code) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.pre_id == pre_id,
                                    CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def update(self, crawling_rule_code, value) -> int:
        return CrawlingRuleData.update(value=value).where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def insert(self, crawlingRuleData) -> None:
        CrawlingRuleData.create(pre_id=crawlingRuleData.pre_id, crawling_rule_code=crawlingRuleData.crawling_rule_code,
                                value=crawlingRuleData.value)
