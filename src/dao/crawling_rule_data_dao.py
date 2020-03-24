# coding=utf-8
from src.base.singleton import Singleton
from src.entity.crawling_rule_data import CrawlingRuleData


class CrawlingRuleDataDao(Singleton):
    """
    api parameter dao
    """

    def load(self, id) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.id == id)

    def load_by_crawling_rule_code(self, crawling_rule_code) -> CrawlingRuleData:
        # return CrawlingRuleData.select().where(CrawlingRuleData.crawling_rule_code == crawling_rule_code).execute()
        return CrawlingRuleData.get(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def load_by_pre_id_and_crawling_rule_code(self, pre_id, crawling_rule_code) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.pre_id == pre_id,
                                    CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def update(self, crawling_rule_code, value) -> int:
        return CrawlingRuleData.update(value=value).where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def insert(self, crawlingRuleData) -> int:
        return CrawlingRuleData.insert(pre_id=crawlingRuleData.pre_id,
                                       crawling_rule_code=crawlingRuleData.crawling_rule_code,
                                       value=crawlingRuleData.value, parameter_name=crawlingRuleData.parameter_name,
                                       parameter_code=crawlingRuleData.parameter_code).execute()

    def list(self, crawling_rule_code) -> list:
        return CrawlingRuleData.select().where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)
